from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message

from config import OWNER_ID


def is_admins(func: Callable) -> Callable:
    async def non_admin(c, m: Message):
        if m.from_user.id == OWNER_ID:
            return await func(c, m)

        try:
            admin = await c.get_chat_member(m.chat.id, m.from_user.id)
            if admin.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                return await func(c, m)
        except:
            pass

    return non_admin 
