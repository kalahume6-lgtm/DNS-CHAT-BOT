import asyncio
import random
import time
import psutil
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import OWNER_ID, OWNER_USERNAME
from DNSCHAT import _boot_, get_readable_time, DNSCHAT, db, LOGGER
from DNSCHAT.database.chats import get_served_chats, add_served_chat
from DNSCHAT.database.users import get_served_users, add_served_user
from DNSCHAT.modules.helpers.inline import get_start_bot
    START,
    CLOSE_BTN,
    HELP_BTN,
    HELP_READ,
    SOURCE_READ,
)

status_db = db.chatbot_status_db.status
BOT_IMG = "https://files.catbox.moe/ugp6i0.jpg"


def get_start_buttons():
    buttons = []
    if DNSCHAT.username:
        buttons.append([
            InlineKeyboardButton(
                "Add me to group",
                url=f"https://t.me/{DNSCHAT.username}?startgroup=true",
            )
        ])
    buttons.append([
        InlineKeyboardButton("Help", callback_data="HELP"),
        InlineKeyboardButton("Close", callback_data="CLOSE"),
    ])
    return InlineKeyboardMarkup(buttons)


async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    UP = get_readable_time(bot_uptime)
    return UP, f"{cpu}%", f"{mem}%", f"{disk}%"


@DNSCHAT.on_message(filters.command(["start", "aistart"]))
async def start_handler(_, m: Message):
    try:
        users = len(await get_served_users())
        chats = len(await get_served_chats())
        UP, _, _, _ = await bot_sys_stats()

        text = (
            f"**Hey {m.from_user.mention}!**\n\n"
            f"{DNSCHAT.mention or 'Bot'} is alive\n\n"
            f"Users: `{users}`\n"
            f"Chats: `{chats}`\n"
            f"Uptime: `{UP}`\n\n"
            f"Commands: /help /ping /repo /stats /id"
        )

        try:
            await m.reply_photo(
                photo=BOT_IMG,
                caption=text,
                reply_markup=get_start_buttons(),
            )
        except Exception:
            await m.reply_text(text, reply_markup=get_start_buttons())

        if m.chat.type == ChatType.PRIVATE:
            await add_served_user(m.from_user.id)
        else:
            await add_served_chat(m.chat.id)

    except Exception as e:
        LOGGER.error(f"start error: {e}")
        await m.reply_text(f"Bot alive. Error: `{e}`")


@DNSCHAT.on_message(filters.command("help"))
async def help_handler(_, m: Message):
    try:
        await m.reply_text(
            HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
            disable_web_page_preview=True,
        )
    except Exception as e:
        await m.reply_text(f"Help error: `{e}`")


@DNSCHAT.on_message(filters.command("repo"))
async def repo_handler(_, m: Message):
    try:
        await m.reply_text(
            SOURCE_READ,
            reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
            disable_web_page_preview=True,
        )
    except Exception as e:
        await m.reply_text(
            "Repo: https://github.com/kalahume6-lgtm/DNS-CHAT-BOT\n"
            f"Error: `{e}`"
        )


@DNSCHAT.on_message(filters.command("ping"))
async def ping_handler(_, message: Message):
    start = datetime.now()
    msg = await message.reply_text("Pinging...")
    ms = (datetime.now() - start).microseconds / 1000
    UP, CPU, RAM, DISK = await bot_sys_stats()
    await msg.edit_text(
        f"**Pong!** `{ms}` ms\n"
        f"CPU: {CPU} | RAM: {RAM}\n"
        f"DISK: {DISK} | UP: {UP}"
    )


@DNSCHAT.on_message(filters.command("stats"))
async def stats_handler(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    me = await cli.get_me()
    await message.reply_text(
        f"**{me.first_name} Stats**\n\n"
        f"Chats: `{chats}`\n"
        f"Users: `{users}`"
    )


@DNSCHAT.on_message(filters.command("id"))
async def id_handler(_, message: Message):
    text = (
        f"**Your ID:** `{message.from_user.id}`\n"
        f"**Chat ID:** `{message.chat.id}`\n"
        f"**Message ID:** `{message.id}`"
    )
    if message.reply_to_message and message.reply_to_message.from_user:
        text += (
            f"\n**Replied User:** `{message.reply_to_message.from_user.id}`"
        )
    await message.reply_text(text)


@DNSCHAT.on_message(filters.new_chat_members)
async def welcome_handler(client, message: Message):
    await add_served_chat(message.chat.id)
    try:
        for member in message.new_chat_members:
            if member.id == DNSCHAT.id:
                await message.reply_text(
                    f"**Thanks for adding {DNSCHAT.mention}!**\n"
                    f"Use /chatbot to enable chatbot."
                )
    except Exception as e:
        LOGGER.error(f"welcome error: {e}")


IS_BROADCASTING = False
broadcast_lock = asyncio.Lock()


@DNSCHAT.on_message(
    filters.command(["broadcast", "gcast"])
    & filters.user(int(OWNER_ID) if OWNER_ID else 0)
)
async def broadcast_handler(client, message):
    global IS_BROADCASTING
    async with broadcast_lock:
        if IS_BROADCASTING:
            return await message.reply_text("Broadcast already running.")

        IS_BROADCASTING = True
        try:
            if not message.reply_to_message and len(message.command) < 2:
                return await message.reply_text(
                    "Reply to a message or use:\n`/broadcast your text`"
                )

            await message.reply_text("Broadcasting...")
            sent = 0

            if message.reply_to_message:
                content = message.reply_to_message
                for chat in await get_served_chats():
                    try:
                        await DNSCHAT.forward_messages(
                            int(chat["chat_id"]),
                            message.chat.id,
                            [content.id],
                        )
                        sent += 1
                    except FloodWait as e:
                        await asyncio.sleep(int(e.value))
                    except Exception:
                        pass
            else:
                text = message.text.split(None, 1)[1]
                for chat in await get_served_chats():
                    try:
                        await DNSCHAT.send_message(int(chat["chat_id"]), text)
                        sent += 1
                    except FloodWait as e:
                        await asyncio.sleep(int(e.value))
                    except Exception:
                        pass

            await message.reply_text(f"Broadcast sent to `{sent}` chats.")
        finally:
            IS_BROADCASTING = False
