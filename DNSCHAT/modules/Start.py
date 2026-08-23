import asyncio
import logging
import random
import time
import psutil
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.errors import FloodWait, ChatAdminRequired
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

from config import OWNER_ID, MONGO_URL, OWNER_USERNAME
from DNSCHAT import _boot_, get_readable_time, DNSCHAT, mongo, db
from DNSCHAT.database.chats import get_served_chats, add_served_chat
from DNSCHAT.database.users import get_served_users, add_served_user
from DNSCHAT.modules.helpers import (
    START,
    START_BOT,
    PNG_BTN,
    CLOSE_BTN,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
)

# ========== Standardized DB (chatbot.py ke saath same) ==========
chatai = db.WordDb
lang_db = db.ChatLangDb.LangCollection
status_db = db.chatbot_status_db.status

GSTART = """**ʜᴇʏ ᴅᴇᴀʀ {}**

**ᴛʜᴀɴᴋs ғᴏʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ʏᴏᴜ ᴄᴀɴ ᴄʜᴀɴɢᴇ ʟᴀɴɢᴜᴀɢᴇ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs.**
**ᴄʟɪᴄᴋ ᴀɴᴅ sᴇʟᴇᴄᴛ ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ ʟᴀɴɢᴜᴀɢᴇ ᴛᴏ sᴇᴛ ᴄʜᴀᴛ ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ʙᴏᴛ ʀᴇᴘʟʏ.**

**ᴛʜᴀɴᴋ ʏᴏᴜ ᴘʟᴇᴀsᴇ ᴇɴᴊᴏʏ.**"""

STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

EMOJIOS = ["💣", "💥", "🪄", "🧨", "⚡", "🤡", "👻", "🎃", "🎩", "🕊"]

BOT = "https://files.catbox.moe/ugp6i0.jpg"
IMG = [
    "https://graph.org/file/210751796ff48991b86a3.jpg",
    "https://graph.org/file/7b4924be4179f70abcf33.jpg",
    "https://graph.org/file/f6d8e64246bddc26b4f66.jpg",
    "https://graph.org/file/63d3ec1ca2c965d6ef210.jpg",
    "https://graph.org/file/9f12dc2a668d40875deb5.jpg",
    "https://graph.org/file/0f89cd8d55fd9bb5130e1.jpg",
    "https://graph.org/file/e5eb7673737ada9679b47.jpg",
    "https://graph.org/file/2e4dfe1fa5185c7ff1bfd.jpg",
    "https://graph.org/file/36af423228372b8899f20.jpg",
    "https://graph.org/file/c698fa9b221772c2a4f3a.jpg",
    "https://graph.org/file/61b08f41855afd9bed0ab.jpg",
    "https://graph.org/file/744b1a83aac76cb3779eb.jpg",
    "https://graph.org/file/814cd9a25dd78480d0ce1.jpg",
    "https://graph.org/file/e8b472bcfa6680f6c6a5d.jpg",
]


async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    UP = f"{get_readable_time(bot_uptime)}"
    CPU = f"{cpu}%"
    RAM = f"{mem}%"
    DISK = f"{disk}%"
    return UP, CPU, RAM, DISK


async def set_default_status(chat_id):
    try:
        if not await status_db.find_one({"chat_id": chat_id}):
            await status_db.insert_one({"chat_id": chat_id, "status": "enabled"})
    except Exception as e:
        print(f"Error setting default status for chat {chat_id}: {e}")


@DNSCHAT.on_message(filters.new_chat_members)
async def welcomejej(client, message: Message):
    await add_served_chat(message.chat.id)
    await set_default_status(message.chat.id)
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    try:
        for member in message.new_chat_members:
            if member.id == DNSCHAT.id:
                reply_markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("sᴇʟᴇᴄᴛ ʟᴀɴɢᴜᴀɢᴇ", callback_data="choose_lang")]]
                )
                await message.reply_photo(
                    photo=random.choice(IMG),
                    caption=START.format(DNSCHAT.mention or "can't mention", users, chats, "0s"),
                    reply_markup=reply_markup,
                )
                chat = message.chat
                try:
                    invitelink = await DNSCHAT.export_chat_invite_link(message.chat.id)
                    link = f"[ɢᴇᴛ ʟɪɴᴋ]({invitelink})"
                except ChatAdminRequired:
                    link = "No Link"

                try:
                    groups_photo = await DNSCHAT.download_media(
                        chat.photo.big_file_id, file_name=f"chatpp{chat.id}.png"
                    )
                    chat_photo = groups_photo if groups_photo else "https://files.catbox.moe/4itjd9.jpg"
                except AttributeError:
                    chat_photo = "https://files.catbox.moe/4itjd9.jpg"

                count = await DNSCHAT.get_chat_members_count(chat.id)
                chats = len(await get_served_chats())
                username = chat.username if chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                msg = (
                    f"**📝𝐌ᴜsɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ**\n\n"
                    f"**📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {chat.title}\n"
                    f"**🍂𝐂ʜᴀᴛ 𝐈ᴅ:** `{chat.id}`\n"
                    f"**🔐𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ:** @{username}\n"
                    f"**🖇️𝐆ʀᴏᴜᴘ 𝐋ɪɴᴋ:** {link}\n"
                    f"**📈𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs:** {count}\n"
                    f"**🤔𝐀ᴅᴅᴇᴅ 𝐁ʏ:** {message.from_user.mention}\n\n"
                    f"**ᴛᴏᴛᴀʟ ᴄʜᴀᴛs :** {chats}"
                )

                if OWNER_ID:
                    try:
                        await DNSCHAT.send_photo(
                            int(OWNER_ID),
                            photo=chat_photo,
                            caption=msg,
                            reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton(
                                    f"{message.from_user.first_name}",
                                    user_id=message.from_user.id
                                )]]
                            ),
                        )
                    except Exception as e:
                        logging.info(f"Error sending to owner: {e}")

    except Exception as e:
        logging.info(f"Error: {e}")


@DNSCHAT.on_message(filters.command(["start", "aistart"]))
async def start(_, m: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(text=random.choice(EMOJIOS))
        await asyncio.sleep(0.5)

        for text in [
            "**__ᴅ__**", "**__ᴅι__**", "**__ᴅιи__**", "**__ᴅιиg__**",
            "**__ᴅιиg ᴅ__**", "**__ᴅιиg ᴅσ__**", "**__ᴅιиg ᴅσи__**",
            "**__ᴅιиg ᴅσиg__**", "**__ᴅιиg ᴅσиg ꨄ︎__**",
            "**__ᴅιиg ᴅσиg ꨄ︎ ѕ__**", "**__ᴅιиg ᴅσиg ꨄ sт__**",
            "**__ᴅιиg ᴅσиg ꨄ︎ ѕтα__**", "**__ᴅιиg ᴅσиg ꨄ︎ ѕтαя__**",
            "**__ᴅιиg ᴅσиg ꨄ sтαят__**", "**__ᴅιиg ᴅσиg ꨄ︎ sтαятι__**",
            "**__ᴅιиg ᴅσиg ꨄ︎ sтαятιи__**", "**__ᴅιиg ᴅσиg ꨄ sтαятιиg__**",
            "**__ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg.__**", "**__ᴅιиg ᴅσиg ꨄ sтαятιиg.....__**",
        ]:
            await accha.edit(text)
            await asyncio.sleep(0.01)

        await accha.delete()

        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        chat_photo = BOT
        if m.chat.photo:
            try:
                userss_photo = await DNSCHAT.download_media(m.chat.photo.big_file_id)
                await umm.delete()
                if userss_photo:
                    chat_photo = userss_photo
            except AttributeError:
                chat_photo = BOT

        users = len(await get_served_users())
        chats = len(await get_served_chats())
        UP, CPU, RAM, DISK = await bot_sys_stats()
        await m.reply_photo(
            photo=chat_photo,
            caption=START.format(DNSCHAT.mention or "can't mention", users, chats, UP),
            reply_markup=InlineKeyboardMarkup(START_BOT),
        )
        await add_served_user(m.chat.id)

        if OWNER_ID:
            try:
                keyboard = InlineKeyboardMarkup(
                    [[InlineKeyboardButton(f"{m.chat.first_name}", user_id=m.chat.id)]]
                )
                await DNSCHAT.send_photo(
                    int(OWNER_ID),
                    photo=chat_photo,
                    caption=(
                        f"{m.from_user.mention} ʜᴀs sᴛᴀʀᴛᴇᴅ ʙᴏᴛ.\n\n"
                        f"**ɴᴀᴍᴇ :** {m.chat.first_name}\n"
                        f"**ᴜsᴇʀɴᴀᴍᴇ :** @{m.chat.username}\n"
                        f"**ɪᴅ :** {m.chat.id}\n\n"
                        f"**ᴛᴏᴛᴀʟ ᴜsᴇʀs :** {users}"
                    ),
                    reply_markup=keyboard,
                )
            except Exception:
                pass

    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=GSTART.format(m.from_user.mention or "can't mention"),
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@DNSCHAT.on_message(filters.command("help"))
async def help(client: Client, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@DNSCHAT.on_message(filters.command("repo"))
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@DNSCHAT.on_message(filters.command("ping"))
async def ping(_, message: Message):
    start = datetime.now()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=(
            f"нey вαву!!\n{DNSCHAT.name} ᴄʜᴀᴛʙᴏᴛ ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n\n"
            f"**➥** `{ms}` ms\n"
            f"**➲ ᴄᴘᴜ:** {CPU}\n"
            f"**➲ ʀᴀᴍ:** {RAM}\n"
            f"**➲ ᴅɪsᴋ:** {DISK}\n"
            f"**➲ ᴜᴘᴛɪᴍᴇ »** {UP}\n\n"
            f"<b>||**๏ мαdє ωιтн ❣️ ву [Rudra ✯ ᴏᴡɴᴇʀ](https://t.me/{OWNER_USERNAME or 'RU_DRA_098'}) **||</b>"
        ),
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)


@DNSCHAT.on_message(filters.command("stats"))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""{(await cli.get_me()).mention} ᴄʜᴀᴛʙᴏᴛ sᴛᴀᴛs:

➻ **ᴄʜᴀᴛs :** {chats}
➻ **ᴜsᴇʀs :** {users}"""
    )


@DNSCHAT.on_message(filters.command("id"))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[ᴍᴇssᴀɢᴇ ɪᴅ:]({message.link})** `{message_id}`\n"
    text += f"**[ʏᴏᴜʀ ɪᴅ:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[ᴜsᴇʀ ɪᴅ:](tg://user?id={user_id})** `{user_id}`\n"
        except Exception:
            return await message.reply_text("ᴛʜɪs ᴜsᴇʀ ᴅᴏᴇsɴ'ᴛ ᴇxɪsᴛ.", quote=True)

    text += f"**[ᴄʜᴀᴛ ɪᴅ:](https://t.me/{chat.username or ''})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ:]({reply.link})** `{reply.id}`\n"
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ɪᴅ:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"ᴛʜᴇ ғᴏʀᴡᴀʀᴅᴇᴅ ᴄʜᴀɴɴᴇʟ, {reply.forward_from_chat.title}, ʜᴀs ᴀɴ ɪᴅ ᴏғ `{reply.forward_from_chat.id}`\n\n"

    if reply and reply.sender_chat:
        text += f"ɪᴅ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴄʜᴀᴛ/ᴄʜᴀɴɴᴇʟ, ɪs `{reply.sender_chat.id}`"

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.DEFAULT,
    )


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

AUTO_SLEEP = 5
IS_BROADCASTING = False
broadcast_lock = asyncio.Lock()

BROADCAST_FLAGS = ["-pinloud", "-nogroup", "-user", "-pin"]


@DNSCHAT.on_message(
    filters.command(["broadcast", "gcast"]) & filters.user(int(OWNER_ID) if OWNER_ID else 0)
)
async def broadcast_message(client, message):
    global IS_BROADCASTING
    async with broadcast_lock:
        if IS_BROADCASTING:
            return await message.reply_text(
                "A broadcast is already in progress. Please wait for it to complete."
            )

        IS_BROADCASTING = True
        try:
            try:
                query = message.text.split(None, 1)[1].strip()
            except IndexError:
                query = message.text.strip()
            except Exception as eff:
                return await message.reply_text(f"**Error**: {eff}")

            try:
                if message.reply_to_message:
                    broadcast_content = message.reply_to_message
                    broadcast_type = "reply"
                    flags = {flag: flag in query for flag in BROADCAST_FLAGS}
                else:
                    if len(message.command) < 2:
                        return await message.reply_text(
                            "**Please provide text after the command or reply to a message for broadcasting.**"
                        )

                    flags = {flag: flag in query for flag in BROADCAST_FLAGS}

                    for flag in BROADCAST_FLAGS:
                        query = query.replace(flag, "").strip()

                    if not query:
                        return await message.reply_text(
                            "Please provide a valid text message or a flag: -pin, -nogroup, -pinloud, -user"
                        )

                    broadcast_content = query
                    broadcast_type = "text"

                if flags.get("-pinloud", False):
                    flags["-pin"] = False

                await message.reply_text("**Started broadcasting...**")

                if not flags.get("-nogroup", False):
                    sent = 0
                    pin_count = 0
                    chats = await get_served_chats()

                    for chat in chats:
                        chat_id = int(chat["chat_id"])
                        if chat_id == message.chat.id:
                            continue
                        try:
                            if broadcast_type == "reply":
                                m = (await DNSCHAT.forward_messages(
                                    chat_id, message.chat.id, [broadcast_content.id]
                                ))[0]
                            else:
                                m = await DNSCHAT.send_message(chat_id, text=broadcast_content)
                            sent += 1

                            if flags.get("-pin", False) or flags.get("-pinloud", False):
                                try:
                                    await m.pin(disable_notification=flags.get("-pin", False))
                                    pin_count += 1
                                except Exception as e:
                                    logger.error(f"Failed to pin message in chat {chat_id}: {e}")

                        except FloodWait as e:
                            flood_time = int(e.value)
                            logger.warning(f"FloodWait of {flood_time} seconds for chat {chat_id}.")
                            if flood_time > 200:
                                continue
                            await asyncio.sleep(flood_time)
                        except Exception as e:
                            logger.error(f"Error broadcasting to chat {chat_id}: {e}")
                            continue

                    await message.reply_text(
                        f"**Broadcasted to {sent} chats and pinned in {pin_count} chats.**"
                    )

                if flags.get("-user", False):
                    susr = 0
                    users = await get_served_users()

                    for user in users:
                        user_id = int(user["user_id"])
                        try:
                            if broadcast_type == "reply":
                                m = (await DNSCHAT.forward_messages(
                                    user_id, message.chat.id, [broadcast_content.id]
                                ))[0]
                            else:
                                m = await DNSCHAT.send_message(user_id, text=broadcast_content)
                            susr += 1

                        except FloodWait as e:
                            flood_time = int(e.value)
                            logger.warning(f"FloodWait of {flood_time} seconds for user {user_id}.")
                            if flood_time > 200:
                                continue
                            await asyncio.sleep(flood_time)
                        except Exception as e:
                            logger.error(f"Error broadcasting to user {user_id}: {e}")
                            continue

                    await message.reply_text(f"**Broadcasted to {susr} users.**")

            finally:
                IS_BROADCASTING = False
        except Exception:
            IS_BROADCASTING = False
            raise
