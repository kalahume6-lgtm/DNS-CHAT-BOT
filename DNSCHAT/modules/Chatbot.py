import random
from pyrogram import Client, filters
from pyrogram.errors import MessageEmpty
from pyrogram.enums import ChatAction
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    CallbackQuery,
)
from deep_translator import GoogleTranslator

from DNSCHAT.database.chats import add_served_chat
from DNSCHAT.database.users import add_served_user
from DNSCHAT import DNSCHAT, db, LOGGER
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

chatai = db.WordDb
lang_db = db.ChatLangDb.LangCollection
status_db = db.chatbot_status_db.status

IGNORE_COMMANDS = [
    "start", "aistart", "help", "repo", "ping", "stats", "id",
    "broadcast", "gcast", "chatbot", "status", "lang", "language",
    "setlang", "resetlang", "nolang", "shayri", "gf", "bf",
    "sari", "shari", "love",
]


def not_bot_command(_, __, message):
    if not message or not message.text:
        return True
    text = message.text.strip()
    if text.startswith("/"):
        cmd = text[1:].split("@")[0].split()[0].lower()
        if cmd in IGNORE_COMMANDS:
            return False
    return True


command_filter = filters.create(not_bot_command)


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
    "english": "en",
    "hindi": "hi",
    "russian": "ru",
    "spanish": "es",
    "arabic": "ar",
    "turkish": "tr",
    "german": "de",
    "french": "fr",
    "italian": "it",
    "persian": "fa",
    "indonesian": "id",
    "portuguese": "pt",
    "korean": "ko",
    "japanese": "ja",
    "urdu": "ur",
    "bengali": "bn",
    "telugu": "te",
    "marathi": "mr",
    "gujarati": "gu",
    "kannada": "kn",
    "malayalam": "ml",
    "punjabi": "pa",
    "tamil": "ta",
}


def generate_language_buttons(languages_dict):
    buttons = []
    current_row = []
    for lang, code in languages_dict.items():
        current_row.append(
            InlineKeyboardButton(lang.capitalize(), callback_data=f"setlang_{code}")
        )
        if len(current_row) == 4:
            buttons.append(current_row)
            current_row = []
    if current_row:
        buttons.append(current_row)
    return InlineKeyboardMarkup(buttons)


async def get_chat_language(chat_id):
    chat_lang = await lang_db.find_one({"chat_id": chat_id})
    if chat_lang and "language" in chat_lang:
        return chat_lang["language"]
    return "en"


@DNSCHAT.on_message(filters.command(["lang", "language", "setlang"]))
async def set_language(client: Client, message: Message):
    await message.reply_text(
        "Please select your chat language:",
        reply_markup=generate_language_buttons(languages),
    )


@DNSCHAT.on_callback_query(filters.regex(r"setlang_"))
async def language_selection_callback(client: Client, callback_query: CallbackQuery):
    lang_code = callback_query.data.split("_")[1]
    chat_id = callback_query.message.chat.id
    if lang_code in languages.values():
        await lang_db.update_one(
            {"chat_id": chat_id},
            {"$set": {"language": lang_code}},
            upsert=True,
        )
        await callback_query.answer(
            f"Language set to {lang_code.title()}.", show_alert=True
        )
        await callback_query.message.edit_text(
            f"Chat language has been set to {lang_code.title()}."
        )
    else:
        await callback_query.answer("Invalid language selection.", show_alert=True)


@DNSCHAT.on_message(filters.command(["resetlang", "nolang"]))
async def reset_language(client: Client, message: Message):
    chat_id = message.chat.id
    await lang_db.update_one(
        {"chat_id": chat_id},
        {"$set": {"language": "nolang"}},
        upsert=True,
    )
    await message.reply_text(
        "**Bot language has been reset in this chat to mix language.**"
    )


@DNSCHAT.on_message(filters.command("chatbot"))
async def chatbot_command(client: Client, message: Message):
    chat_id = message.chat.id
    existing = await status_db.find_one({"chat_id": chat_id})
    if not existing:
        await status_db.update_one(
            {"chat_id": chat_id},
            {"$set": {"status": "disabled"}},
            upsert=True,
        )
    await message.reply_text(
        f"Chat: {message.chat.title or 'Private'}\n"
        f"**Choose an option to enable/disable the chatbot.**",
        reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
    )


@DNSCHAT.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    data = query.data
    LOGGER.info(data)

    if data == "HELP":
        await query.message.edit_text(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
            disable_web_page_preview=True,
        )
    elif data == "CLOSE":
        await query.message.delete()
        await query.answer("Closed menu!", show_alert=True)
    elif data == "BACK":
        await query.message.edit(
            text=START.format(DNSCHAT.mention or "Bot", 0, 0, "0s"),
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
    elif data == "SOURCE":
        await query.message.edit(
            text=get_source_read(),
            reply_markup=InlineKeyboardMarkup(BACK),
            disable_web_page_preview=True,
        )
    elif data == "ABOUT":
        await query.message.edit(
            text=get_about_read(),
            reply_markup=InlineKeyboardMarkup(ABOUT_BTN),
            disable_web_page_preview=True,
        )
    elif data == "ADMINS":
        await query.message.edit(
            text=ADMIN_READ,
            reply_markup=InlineKeyboardMarkup(MUSIC_BACK_BTN),
        )
    elif data == "TOOLS_DATA":
        await query.message.edit(
            text=get_tools_data_read(),
            reply_markup=InlineKeyboardMarkup(CHATBOT_BACK),
        )
    elif data == "BACK_HELP":
        await query.message.edit(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
    elif data == "CHATBOT_CMD":
        await query.message.edit(
            text=get_chatbot_read(),
            reply_markup=InlineKeyboardMarkup(CHATBOT_BACK),
        )
    elif data == "CHATBOT_BACK":
        await query.message.edit(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
    elif data == "enable_chatbot":
        chat_id = query.message.chat.id
        await status_db.update_one(
            {"chat_id": chat_id},
            {"$set": {"status": "enabled"}},
            upsert=True,
        )
        await query.answer("Chatbot enabled", show_alert=True)
        await query.edit_message_text(
            f"Chat: {query.message.chat.title or 'Private'}\n"
            f"**Chatbot has been enabled.**"
        )
    elif data == "disable_chatbot":
        chat_id = query.message.chat.id
        await status_db.update_one(
            {"chat_id": chat_id},
            {"$set": {"status": "disabled"}},
            upsert=True,
        )
        await query.answer("Chatbot disabled!", show_alert=True)
        await query.edit_message_text(
            f"Chat: {query.message.chat.title or 'Private'}\n"
            f"**Chatbot has been disabled.**"
        )
    elif data == "choose_lang":
        await query.answer("Choose chatbot language for this chat.", show_alert=True)
        await query.message.edit_text(
            "**Please select your preferred language for the chatbot.**",
            reply_markup=generate_language_buttons(languages),
        )


@DNSCHAT.on_message(filters.incoming & command_filter)
async def chatbot_response(client: Client, message: Message):
    try:
        chat_id = message.chat.id
        chat_status = await status_db.find_one({"chat_id": chat_id})
        is_group = str(message.chat.type) in ("group", "supergroup") or message.chat.type.name in ("GROUP", "SUPERGROUP")

        if chat_status:
            if chat_status.get("status") == "disabled":
                return
        elif is_group:
            return

        if not message.text and not message.sticker:
            return

        replied_to_bot = (
            message.reply_to_message
            and message.reply_to_message.from_user
            and message.reply_to_message.from_user.id == DNSCHAT.id
        )

        if replied_to_bot or not message.reply_to_message:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)
            reply_data = await get_reply(message.text or "")

            if reply_data:
                response_text = reply_data["text"]
                chat_lang = await get_chat_language(chat_id)

                if not chat_lang or chat_lang == "nolang":
                    translated_text = response_text
                else:
                    try:
                        translated_text = GoogleTranslator(
                            source="auto", target=chat_lang
                        ).translate(response_text)
                    except Exception:
                        translated_text = response_text

                check = reply_data.get("check", "none")
                if check == "sticker":
                    await message.reply_sticker(reply_data["text"])
                elif check == "photo":
                    await message.reply_photo(reply_data["text"])
                elif check == "video":
                    await message.reply_video(reply_data["text"])
                elif check == "audio":
                    await message.reply_audio(reply_data["text"])
                elif check == "gif":
                    await message.reply_animation(reply_data["text"])
                else:
                    await message.reply_text(translated_text)
            else:
                await message.reply_text(
                    "**I don't understand. what are you saying??**"
                )

        if message.reply_to_message and message.text:
            await save_reply(message.reply_to_message, message)

        if is_group:
            await add_served_chat(chat_id)
        elif message.from_user:
            await add_served_user(message.from_user.id)

    except MessageEmpty:
        try:
            await message.reply_text("...")
        except Exception:
            pass
    except Exception as e:
        LOGGER.error(f"chatbot_response error: {e}")


async def save_reply(original_message: Message, reply_message: Message):
    try:
        if not original_message or not original_message.text:
            return

        word = original_message.text

        if reply_message.sticker:
            doc = {
                "word": word,
                "text": reply_message.sticker.file_id,
                "check": "sticker",
            }
        elif reply_message.photo:
            doc = {
                "word": word,
                "text": reply_message.photo.file_id,
                "check": "photo",
            }
        elif reply_message.video:
            doc = {
                "word": word,
                "text": reply_message.video.file_id,
                "check": "video",
            }
        elif reply_message.audio:
            doc = {
                "word": word,
                "text": reply_message.audio.file_id,
                "check": "audio",
            }
        elif reply_message.animation:
            doc = {
                "word": word,
                "text": reply_message.animation.file_id,
                "check": "gif",
            }
        elif reply_message.text:
            doc = {
                "word": word,
                "text": reply_message.text,
                "check": "none",
            }
        else:
            return

        exists = await chatai.find_one(doc)
        if not exists:
            await chatai.insert_one(doc)
    except Exception as e:
        LOGGER.error(f"Error in save_reply: {e}")


async def get_reply(word: str):
    try:
        if not word:
            return None
        results = await chatai.find({"word": word}).to_list(length=50)
        if results:
            return random.choice(results)
        return None
    except Exception as e:
        LOGGER.error(f"Error in get_reply: {e}")
        return None
