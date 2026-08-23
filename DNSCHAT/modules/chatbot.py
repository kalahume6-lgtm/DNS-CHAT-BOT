import random
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import MessageEmpty
from pyrogram.enums import ChatAction, ChatMemberStatus as CMS
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    CallbackQuery,
)
from deep_translator import GoogleTranslator

from DNSCHAT.database.chats import add_served_chat
from DNSCHAT.database.users import add_served_user
from DNSCHAT import DNSCHAT, mongo, db, LOGGER
from DNSCHAT.modules.helpers import (
    CHATBOT_ON,
    ABOUT_BTN,
    ADMIN_READ,
    BACK,
    CHATBOT_BACK,
    DEV_OP,
    HELP_BTN,
    HELP_READ,
    MUSIC_BACK_BTN,
    START,
    get_about_read,
    get_chatbot_read,
    get_source_read,
    get_tools_data_read,
)
import config

# ========== Standardized Database Collections ==========
chatai = db.WordDb
lang_db = db.ChatLangDb.LangCollection
status_db = db.chatbot_status_db.status


@DNSCHAT.on_message(filters.command("status"))
async def status_command(client: Client, message: Message):
    chat_id = message.chat.id
    chat_status = await status_db.find_one({"chat_id": chat_id})

    if chat_status:
        current_status = chat_status.get("status", "not found")
        await message.reply(f"Chatbot status for this chat: **{current_status}**")
    else:
        await message.reply("No status found for this chat.")


languages = {
    # Top languages
    'english': 'en', 'hindi': 'hi', 'myanmar': 'my', 'russian': 'ru', 'spanish': 'es',
    'arabic': 'ar', 'turkish': 'tr', 'german': 'de', 'french': 'fr',
    'italian': 'it', 'persian': 'fa', 'indonesian': 'id', 'portuguese': 'pt',
    'ukrainian': 'uk', 'filipino': 'tl', 'korean': 'ko', 'japanese': 'ja',
    'polish': 'pl', 'vietnamese': 'vi', 'thai': 'th', 'dutch': 'nl',

    # Bihar / India
    'bhojpuri': 'bho', 'maithili': 'mai', 'urdu': 'ur',
    'bengali': 'bn', 'angika': 'anp', 'sanskrit': 'sa',
    'oriya': 'or', 'nepali': 'ne', 'santhali': 'sat',
    'telugu': 'te', 'marathi': 'mr', 'gujarati': 'gu', 'kannada': 'kn',
    'malayalam': 'ml', 'odia': 'or', 'punjabi': 'pa', 'assamese': 'as',
    'tamil': 'ta',

    # Others
    'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW',
    'hebrew': 'iw', 'swedish': 'sv', 'greek': 'el', 'czech': 'cs',
    'romanian': 'ro', 'hungarian': 'hu', 'finnish': 'fi', 'danish': 'da',
    'norwegian': 'no', 'slovak': 'sk', 'croatian': 'hr', 'serbian': 'sr',
    'bulgarian': 'bg', 'ukrainian': 'uk', 'swahili': 'sw', 'afrikaans': 'af',
}


def generate_language_buttons(languages):
    buttons = []
    current_row = []
    for lang, code in languages.items():
        current_row.append(InlineKeyboardButton(lang.capitalize(), callback_data=f'setlang_{code}'))
        if len(current_row) == 4:
            buttons.append(current_row)
            current_row = []
    if current_row:
        buttons.append(current_row)
    return InlineKeyboardMarkup(buttons)


async def get_chat_language(chat_id):
    chat_lang = await lang_db.find_one({"chat_id": chat_id})
    return chat_lang["language"] if chat_lang and "language" in chat_lang else "en"


@DNSCHAT.on_message(filters.command(["lang", "language", "setlang"]))
async def set_language(client: Client, message: Message):
    await message.reply_text(
        "Please select your chat language:",
        reply_markup=generate_language_buttons(languages)
    )


@DNSCHAT.on_callback_query(filters.regex(r"setlang_"))
async def language_selection_callback(client: Client, callback_query: CallbackQuery):
    lang_code = callback_query.data.split("_")[1]
    chat_id = callback_query.message.chat.id
    if lang_code in languages.values():
        await lang_db.update_one({"chat_id": chat_id}, {"$set": {"language": lang_code}}, upsert=True)
        await callback_query.answer(f"Your chat language has been set to {lang_code.title()}.", show_alert=True)
        await callback_query.message.edit_text(f"Chat language has been set to {lang_code.title()}.")
    else:
        await callback_query.answer("Invalid language selection.", show_alert=True)


@DNSCHAT.on_message(filters.command(["resetlang", "nolang"]))
async def reset_language(client: Client, message: Message):
    chat_id = message.chat.id
    await lang_db.update_one({"chat_id": chat_id}, {"$set": {"language": "nolang"}}, upsert=True)
    await message.reply_text("**Bot language has been reset in this chat to mix language.**")


@DNSCHAT.on_message(filters.command("chatbot"))
async def chatbot_command(client: Client, message: Message):
    chat_id = message.chat.id
    existing = await status_db.find_one({"chat_id": chat_id})
    if not existing:
        await status_db.update_one(
            {"chat_id": chat_id}, {"$set": {"status": "disabled"}}, upsert=True
        )
    await message.reply_text(
        f"Chat: {message.chat.title or 'Private'}\n**Choose an option to enable/disable the chatbot.**",
        reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
    )


@DNSCHAT.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    LOGGER.info(query.data)

    if query.data == "HELP":
        await query.message.edit_text(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
            disable_web_page_preview=True,
        )

    elif query.data == "CLOSE":
        await query.message.delete()
        await query.answer("Closed menu!", show_alert=True)

    elif query.data == "BACK":
        await query.message.edit(
            text=START.format(DNSCHAT.mention or "Bot", 0, 0, "0s"),
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )

    elif query.data == "SOURCE":
        await query.message.edit(
            text=get_source_read(),
            reply_markup=InlineKeyboardMarkup(BACK),
            disable_web_page_preview=True,
        )

    elif query.data == "ABOUT":
        await query.message.edit(
            text=get_about_read(),
            reply_markup=InlineKeyboardMarkup(ABOUT_BTN),
            disable_web_page_preview=True,
        )

    elif query.data == "ADMINS":
        await query.message.edit(
            text=ADMIN_READ,
            reply_markup=InlineKeyboardMarkup(MUSIC_BACK_BTN),
        )

    elif query.data == "TOOLS_DATA":
        await query.message.edit(
            text=get_tools_data_read(),
            reply_markup=InlineKeyboardMarkup(CHATBOT_BACK),
        )

    elif query.data == "BACK_HELP":
        await query.message.edit(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )

    elif query.data == "CHATBOT_CMD":
        await query.message.edit(
            text=get_chatbot_read(),
            reply_markup=InlineKeyboardMarkup(CHATBOT_BACK),
        )

    elif query.data == "CHATBOT_BACK":
        await query.message.edit(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )

    elif query.data == "enable_chatbot":
        chat_id = query.message.chat.id
        await status_db.update_one({"chat_id": chat_id}, {"$set": {"status": "enabled"}}, upsert=True)
        await query.answer("Chatbot enabled ✅", show_alert=True)
        await query.edit_message_text(
            f"Chat: {query.message.chat.title or 'Private'}\n**Chatbot has been enabled.**"
        )

    elif query.data == "disable_chatbot":
        chat_id = query.message.chat.id
        await status_db.update_one({"chat_id": chat_id}, {"$set": {"status": "disabled"}}, upsert=True)
        await query.answer("Chatbot disabled!", show_alert=True)
        await query.edit_message_text(
            f"Chat: {query.message.chat.title or 'Private'}\n**Chatbot has been disabled.**"
        )

    elif query.data == "choose_lang":
        await query.answer("Choose chatbot language for this chat.", show_alert=True)
        await query.message.edit_text(
            "**Please select your preferred language for the chatbot.**",
            reply_markup=generate_language_buttons(languages)
        )


@DNSCHAT.on_message(filters.incoming)
async def chatbot_response(client: Client, message: Message):
    try:
        chat_id = message.chat.id
        chat_status = await status_db.find_one({"chat_id": chat_id})
        is_group = message.chat.type in ("group", "supergroup")

        if chat_status:
            if chat_status.get("status") == "disabled":
                return
        elif is_group:
            # New group with no status → default OFF
            return

        if message.text and any(message.text.startswith(prefix) for prefix in ["!", "/", ".", "?", "@", "#"]):
            if is_group:
                return await add_served_chat(message.chat.id)
            else:
                return await add_served_user(message.chat.id)

        replied_to_bot = (
            message.reply_to_message
            and message.reply_to_message.from_user
            and message.reply_to_message.from_user.id == DNSCHAT.id
        )
        if replied_to_bot or not message.reply_to_message:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)
            reply_data = await get_reply(message.text)

            if reply_data:
                response_text = reply_data["text"]
                chat_lang = await get_chat_language(chat_id)

                if not chat_lang or chat_lang == "nolang":
                    translated_text = response_text
                else:
                    try:
                        translated_text = GoogleTranslator(source="auto", target=chat_lang).translate(response_text)
                    except Exception:
                        translated_text = response_text

                if reply_data["check"] == "sticker":
                    await message.reply_sticker(reply_data["text"])
                elif reply_data["check"] == "photo":
                    await message.reply_photo(reply_data["text"])
                elif reply_data["check"] == "video":
                    await message.reply_video(reply_data["text"])
                elif reply_data["check"] == "audio":
                    await message.reply_audio(reply_data["text"])
                elif reply_data["check"] == "gif":
                    await message.reply_animation(reply_data["text"])
                else:
                    await message.reply_text(translated_text)
            else:
                await message.reply_text("**I don't understand. what are you saying??**")

        if message.reply_to_message:
            await save_reply(message.reply_to_message, message)
    except MessageEmpty:
        return await message.reply_text("🙄🙄")
    except Exception as e:
        LOGGER.error(f"chatbot_response error: {e}")
        return


async def save_reply(original_message: Message, reply_message: Message):
    try:
        if not original_message.text:
            return

        if reply_message.sticker:
            is_chat = await chatai.find_one({
                "word": original_message.text,
                "text": reply_message.sticker.file_id,
                "check": "sticker",
            })
            if not is_chat:
                await chatai.insert_one({
                    "word": original_message.text,
                    "text": reply_message.sticker.file_id,
                    "check": "sticker",
                })

        elif reply_message.photo:
            is_chat = await chatai.find_one({
                "word": original_message.text,
                "text": reply_message.photo.file_id,
                "check": "photo",
            })
            if not is_chat:
                await chatai.insert_one({
                    "word": original_message.text,
                    "text": reply_message.photo.file_id,
                    "check": "photo",
                })

        elif reply_message.video:
            is_chat = await chatai.find_one({
                "word": original_message.text,
                "text": reply_message.video.file_id,
                "check": "video",
            })
            if not is_chat:
                await chatai.insert_one({
                    "word": original_message.text,
                    "text": reply_message.video.file_id,
                    "check": "video",
                })

        elif reply_message.audio:
            is_chat = await chatai.find_one({
                "word": original_message.text,
                "text": reply_message.audio.file_id,
                "check": "audio",
            })
            if not is_chat:
                await chatai.insert_one({
                    "word": original_message.text,
                    "text": reply_message.audio.file_id,
                    "check": "audio",
                })

        elif reply_message.animation:
            is_chat = await chatai.find_one({
                "word": original_message.text,
                "text": reply_message.animation.file_id,
                "check": "gif",
            })
            if not is_chat:
                await chatai.insert_one({
                    "word": original_message.text,
                    "text": reply_message.animation.file_id,
                    "check": "gif",
                })

        elif reply_message.text:
            is_chat = await chatai.find_one({
                "word": original_message.text,
                "text": reply_message.text,
                "check": "none",
            })
            if not is_chat:
                await chatai.insert_one({
                    "word": original_message.text,
                    "text": reply_message.text,
                    "check": "none",
                })

    except Exception as e:
        LOGGER.error(f"Error in save_reply: {e}")


async def get_reply(word: str):
    try:
        if not word:
            return None
        is_chat = await chatai.find({"word": word}).to_list(length=None)
        return random.choice(is_chat) if is_chat else None
    except Exception as e:
        LOGGER.error(f"Error in get_reply: {e}")
        return None
