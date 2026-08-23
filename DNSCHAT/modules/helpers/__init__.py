from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message
from pyrogram import filters

from config import OWNER_ID

# ---------- Admin check decorator ----------
def is_admins(func: Callable) -> Callable:
    async def non_admin(c, m: Message):
        if m.from_user and m.from_user.id == OWNER_ID:
            return await func(c, m)

        try:
            admin = await c.get_chat_member(m.chat.id, m.from_user.id)
            if admin.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                return await func(c, m)
        except Exception:
            pass

    return non_admin


# ---------- Custom on_cmd decorator (Start.py ke liye) ----------
def on_cmd(commands: list | str):
    """
    Simple command decorator.
    Usage: @DNSCHAT.on_cmd(["start", "help"])
    """
    if isinstance(commands, str):
        commands = [commands]

    def decorator(func):
        # Pyrogram client par later attach hoga
        func._commands = commands
        return func

    return decorator


# ---------- Export everything from read & inline ----------
from .read import (
    START,
    HELP_READ,
    ADMIN_READ,
    get_tools_data_read,
    get_chatbot_read,
    get_source_read,
    get_about_read,
    SOURCE_READ,
    CHATBOT_ON,
)

from .inline import (
    START_BOT,
    DEV_OP,
    PNG_BTN,
    BACK,
    HELP_BTN,
    CLOSE_BTN,
    MUSIC_BACK_BTN,
    CHATBOT_BACK,
    HELP_START,
    HELP_BUTN,
    ABOUT_BTN,
    S_BACK,
)

__all__ = [
    "is_admins",
    "on_cmd",
    "START",
    "HELP_READ",
    "ADMIN_READ",
    "get_tools_data_read",
    "get_chatbot_read",
    "get_source_read",
    "get_about_read",
    "SOURCE_READ",
    "CHATBOT_ON",
    "START_BOT",
    "DEV_OP",
    "PNG_BTN",
    "BACK",
    "HELP_BTN",
    "CLOSE_BTN",
    "MUSIC_BACK_BTN",
    "CHATBOT_BACK",
    "HELP_START",
    "HELP_BUTN",
    "ABOUT_BTN",
    "S_BACK",
]
