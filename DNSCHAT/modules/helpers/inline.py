from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL, OWNER_ID
from DNSCHAT import OWNER, DNSCHAT


START_BOT = [
    [
        InlineKeyboardButton(
            text="❖ ᴧᴅᴅ мᴇ ʙᴧʙʏ ❖",
            url=f"https://t.me/{DNSCHAT.username}?startgroup=true" if DNSCHAT.username else "https://t.me/",
        ),
    ],
    [
        InlineKeyboardButton(text="• ❍ᴡɴᴇꝛ •", user_id=OWNER if OWNER else OWNER_ID),
        InlineKeyboardButton(text="• sᴜᴘᴘᴏꝛᴛ •", url=f"https://t.me/{SUPPORT_GRP or 'RU_DRA_098'}"),
    ],
    [
        InlineKeyboardButton(text="⌯ ғᴇᴧᴛᴜʀᴇs ⌯", callback_data="HELP"),
    ],
]


DEV_OP = [
    [
        InlineKeyboardButton(text="• ❍ᴡɴᴇꝛ •", user_id=OWNER if OWNER else OWNER_ID),
        InlineKeyboardButton(text="• sᴜᴘᴘᴏꝛᴛ •", url=f"https://t.me/{SUPPORT_GRP or 'RU_DRA_098'}"),
    ],
    [
        InlineKeyboardButton(
            text="✦ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✦",
            url=f"https://t.me/{DNSCHAT.username}?startgroup=true" if DNSCHAT.username else "https://t.me/",
        ),
    ],
    [
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="☁️ ᴀʙᴏᴜᴛ ☁️", callback_data="ABOUT"),
    ],
]


PNG_BTN = [
    [
        InlineKeyboardButton(
            text="• ᴧᴅᴅ мᴇ ʙᴧʙʏ •",
            url=f"https://t.me/{DNSCHAT.username}?startgroup=true" if DNSCHAT.username else "https://t.me/",
        ),
    ],
    [
        InlineKeyboardButton(
            text="⦿ ᴄʟᴏsᴇ ⦿",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="🐳 ᴄʜᴀᴛʙᴏᴛ 🐳", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="🎄 ᴛᴏᴏʟs 🎄", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


# Yeh important hai — chatbot enable/disable buttons
CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data="enable_chatbot"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data="disable_chatbot"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="sᴏᴏɴ", callback_data="soom"),
    ],
]


S_BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="SBACK"),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
        InlineKeyboardButton(text="🐳 ᴄʟᴏsᴇ 🐳", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="« ʜᴇʟᴘ »",
            url=f"https://t.me/{DNSCHAT.username}?start=help" if DNSCHAT.username else "https://t.me/",
        ),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="🎄 sᴜᴘᴘᴏʀᴛ 🎄", url=f"https://t.me/{SUPPORT_GRP or 'RU_DRA_098'}"),
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="🍾 ᴏᴡɴᴇʀ 🍾", user_id=OWNER if OWNER else OWNER_ID),
    ],
    [
        InlineKeyboardButton(text="🐳 ᴜᴘᴅᴀᴛᴇs 🐳", url=f"https://t.me/{UPDATE_CHNL or SUPPORT_GRP or 'RU_DRA_098'}"),
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK"),
    ],
]
