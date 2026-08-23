import asyncio
import logging
import random
import time
import psutil
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.errors import FloodWait, ChatAdminRequired
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import OWNER_ID, OWNER_USERNAME
from DNSCHAT import _boot_, get_readable_time, DNSCHAT, db, LOGGER
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

status_db = db.chatbot_status_db.status

GSTART = """**ʜᴇʏ ᴅᴇᴀʀ {}**

**ᴛʜᴀɴᴋs ғᴏʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ.**
**ʏᴏᴜ ᴄᴀɴ ᴄʜᴀɴɢᴇ ʟᴀɴɢᴜᴀɢᴇ ʙʏ /lang**

**ᴛʜᴀɴᴋ ʏᴏᴜ ᴘʟᴇᴀsᴇ ᴇɴᴊᴏʏ.**"""

STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

EMOJIOS = ["💣", "💥", "🪄", "🧨", "⚡", "🤡", "👻", "🎃", "🎩", "🕊"]

BOT_IMG = "https://files.catbox.moe/ugp6i0.jpg"
IMG = [
    "https://graph.org/file/210751796ff48991b86a3.jpg",
    "https://graph.org/file/7b4924be4179f70abcf33.jpg",
    "https://graph.org/file/f6d8e64246bddc26b4f66.jpg",
    "https://graph.org/file/63d3ec1ca2c965d6ef210.jpg",
    "https://graph.org/file/9f12dc2a668d40875deb5.jpg",
]


async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    UP = get_readable_time(bot_uptime)
    return UP, f"{cpu}%", f"{mem}%", f"{disk}%"


async def set_default_status(chat_id):
    try:
        if not await status_db.find_one({"chat_id": chat_id}):
            await status_db.insert_one({"chat_id": chat_id, "status": "enabled"})
    except Exception as e:
        LOGGER.error(f"Error setting default status: {e}")


@DNSCHAT.on_message(filters.new_chat_members)
async def welcomejej(client, message: Message):
    await add_served_chat(message.chat.id)
    await set_default_status(message.chat.id)
    try:
        for member in message.new_chat_members:
            if member.id == DNSCHAT.id:
                users = len(await get_served_users())
                chats = len(await get_served_chats())
                await message.reply_photo(
                    photo=random.choice(IMG),
                    caption=START.format(
                        DNSCHAT.mention or "Bot", users, chats, "0s"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("sᴇʟᴇᴄᴛ ʟᴀɴɢᴜᴀɢᴇ", callback_data="choose_lang")]]
                    ),
                )
                if OWNER_ID:
                    try:
                        await DNSCHAT.send_message(
                            int(OWNER_ID),
                            f"**Bot added in:** {message.chat.title}\n**ID:** `{message.chat.id}`\n**By:** {message.from_user.mention}",
                        )
                    except Exception:
                        pass
    except Exception as e:
        LOGGER.error(f"welcome error: {e}")


@DNSCHAT.on_message(filters.command(["start", "aistart"]) & filters.private)
async def start_private(_, m: Message):
    try:
        users = len(await get_served_users())
        chats = len(await get_served_chats())
        UP, CPU, RAM, DISK = await bot_sys_stats()

        await m.reply_photo(
            photo=BOT_IMG,
            caption=START.format(
                DNSCHAT.mention or "Bot", users, chats, UP
            ),
            reply_markup=InlineKeyboardMarkup(START_BOT),
        )
        await add_served_user(m.from_user.id)

        if OWNER_ID and m.from_user.id != int(OWNER_ID):
            try:
                await DNSCHAT.send_message(
                    int(OWNER_ID),
                    f"{m.from_user.mention} started the bot.\n**ID:** `{m.from_user.id}`",
                )
            except Exception:
                pass
    except Exception as e:
        LOGGER.error(f"start_private error: {e}")
        await m.reply_text(f"**Bot is alive!**\nError showing full start: `{e}`")


@DNSCHAT.on_message(filters.command(["start", "aistart"]) & filters.group)
async def start_group(_, m: Message):
    try:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=GSTART.format(m.from_user.mention or "User"),
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)
    except Exception as e:
        LOGGER.error(f"start_group error: {e}")
        await m.reply_text("**Bot is alive in this group!**")


@DNSCHAT.on_message(filters.command("help") & filters.private)
async def help_private(_, m: Message):
    await m.reply_photo(
        photo=random.choice(IMG),
        caption=HELP_READ,
        reply_markup=InlineKeyboardMarkup(HELP_BTN),
    )


@DNSCHAT.on_message(filters.command("help") & filters.group)
async def help_group(_, m: Message):
    await m.reply_text(
        "**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
        reply_markup=InlineKeyboardMarkup(HELP_BUTN),
    )


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
    msg = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    ms = (datetime.now() - start).microseconds / 1000
    await msg.edit_text(
        f"**🏓 Pong!**\n"
        f"**➥** `{ms}` ms\n"
        f"**➲ CPU:** {CPU}\n"
        f"**➲ RAM:** {RAM}\n"
        f"**➲ DISK:** {DISK}\n"
        f"**➲ UPTIME:** {UP}"
    )


@DNSCHAT.on_message(filters.command("stats"))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    me = await cli.get_me()
    await message.reply_text(
        f"**{me.mention} Stats:**\n\n"
        f"➻ **Chats:** {chats}\n"
        f"➻ **Users:** {users}"
    )


@DNSCHAT.on_message(filters.command("id"))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    text = (
        f"**Your ID:** `{your_id}`\n"
        f"**Chat ID:** `{chat.id}`\n"
        f"**Message ID:** `{message.id}`"
    )
    if message.reply_to_message and message.reply_to_message.from_user:
        text += f"\n**Replied User ID:** `{message.reply_to_message.from_user.id}`"
    await message.reply_text(text)


# ========== Broadcast ==========
IS_BROADCASTING = False
broadcast_lock = asyncio.Lock()
BROADCAST_FLAGS = ["-pinloud", "-nogroup", "-user", "-pin"]


@DNSCHAT.on_message(
    filters.command(["broadcast", "gcast"])
    & filters.user(int(OWNER_ID) if OWNER_ID else 0)
)
async def broadcast_message(client, message):
    global IS_BROADCASTING
    async with broadcast_lock:
        if IS_BROADCASTING:
            return await message.reply_text("A broadcast is already in progress.")

        IS_BROADCASTING = True
        try:
            try:
                query = message.text.split(None, 1)[1].strip()
            except IndexError:
                query = ""

            if message.reply_to_message:
                broadcast_content = message.reply_to_message
                broadcast_type = "reply"
                flags = {flag: flag in query for flag in BROADCAST_FLAGS}
            else:
                if len(message.command) < 2:
                    return await message.reply_text(
                        "Reply to a message or give text.\nFlags: `-user` `-pin` `-pinloud` `-nogroup`"
                    )
                flags = {flag: flag in query for flag in BROADCAST_FLAGS}
                for flag in BROADCAST_FLAGS:
                    query = query.replace(flag, "").strip()
                if not query:
                    return await message.reply_text("Please provide text to broadcast.")
                broadcast_content = query
                broadcast_type = "text"

            if flags.get("-pinloud"):
                flags["-pin"] = False

            await message.reply_text("**Started broadcasting...**")

            if not flags.get("-nogroup"):
                sent = pin_count = 0
                for chat in await get_served_chats():
                    chat_id = int(chat["chat_id"])
                    try:
                        if broadcast_type == "reply":
                            m = (
                                await DNSCHAT.forward_messages(
                                    chat_id, message.chat.id, [broadcast_content.id]
                                )
                            )[0]
                        else:
                            m = await DNSCHAT.send_message(chat_id, text=broadcast_content)
                        sent += 1
                        if flags.get("-pin") or flags.get("-pinloud"):
                            try:
                                await m.pin(disable_notification=flags.get("-pin", False))
                                pin_count += 1
                            except Exception:
                                pass
                    except FloodWait as e:
                        if int(e.value) > 200:
                            continue
                        await asyncio.sleep(int(e.value))
                    except Exception:
                        continue
                await message.reply_text(
                    f"**Broadcasted to {sent} chats, pinned in {pin_count}.**"
                )

            if flags.get("-user"):
                susr = 0
                for user in await get_served_users():
                    user_id = int(user["user_id"])
                    try:
                        if broadcast_type == "reply":
                            await DNSCHAT.forward_messages(
                                user_id, message.chat.id, [broadcast_content.id]
                            )
                        else:
                            await DNSCHAT.send_message(user_id, text=broadcast_content)
                        susr += 1
                    except FloodWait as e:
                        if int(e.value) > 200:
                            continue
                        await asyncio.sleep(int(e.value))
                    except Exception:
                        continue
                await message.reply_text(f"**Broadcasted to {susr} users.**")
        finally:
            IS_BROADCASTING = False
