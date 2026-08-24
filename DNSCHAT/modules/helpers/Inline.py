from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL, OWNER_ID
from DNSCHAT import OWNER, DNSCHAT


def _owner_id():
    return OWNER if OWNER else OWNER_ID


def _support():
    return SUPPORT_GRP or "RU_DRA_098"


def _update():
    return UPDATE_CHNL or SUPPORT_GRP or "RU_DRA_098"


def _username():
    return DNSCHAT.username or "YASHIKA_CHAT_BOT"


def get_start_bot():
    return [
        [
            InlineKeyboardButton(
                text="Add me to group",
                url=f"https://t.me/{_username()}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="Owner", user_id=_owner_id()),
            InlineKeyboardButton(text="Support", url=f"https://t.me/{_support()}"),
        ],
        [
            InlineKeyboardButton(text="Features", callback_data="HELP"),
        ],
    ]


def get_dev_op():
    return [
        [
            InlineKeyboardButton(text="Owner", user_id=_owner_id()),
            InlineKeyboardButton(text="Support", url=f"https://t.me/{_support()}"),
        ],
        [
            InlineKeyboardButton(
                text="Add me",
                url=f"https://t.me/{_username()}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="Help", callback_data="HELP"),
        ],
        [
            InlineKeyboardButton(text="About", callback_data="ABOUT"),
        ],
    ]


# Purane names ke liye alias (import break na ho)
START_BOT = None  # runtime pe mat use karo seedha list; Start.py me get_start_bot use hoga
DEV_OP = [
    [InlineKeyboardButton(text="Help", callback_data="HELP")],
    [InlineKeyboardButton(text="About", callback_data="ABOUT")],
]

PNG_BTN = [
    [InlineKeyboardButton(text="Close", callback_data="CLOSE")],
]

BACK = [
    [InlineKeyboardButton(text="Back", callback_data="BACK")],
]

HELP_BTN = [
    [
        InlineKeyboardButton(text="Chatbot", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="Tools", callback_data="TOOLS_DATA"),
    ],
    [InlineKeyboardButton(text="Close", callback_data="CLOSE")],
]

CLOSE_BTN = [
    [InlineKeyboardButton(text="Close", callback_data="CLOSE")],
]

CHATBOT_ON = [
    [
        InlineKeyboardButton(text="Enable", callback_data="enable_chatbot"),
        InlineKeyboardButton(text="Disable", callback_data="disable_chatbot"),
    ],
]

MUSIC_BACK_BTN = [
    [InlineKeyboardButton(text="Soon", callback_data="soom")],
]

S_BACK = [
    [
        InlineKeyboardButton(text="Back", callback_data="SBACK"),
        InlineKeyboardButton(text="Close", callback_data="CLOSE"),
    ],
]

CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="Back", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="Close", callback_data="CLOSE"),
    ],
]

HELP_START = [
    [
        InlineKeyboardButton(text="Help", callback_data="HELP"),
        InlineKeyboardButton(text="Close", callback_data="CLOSE"),
    ],
]

HELP_BUTN = [
    [
        InlineKeyboardButton(text="Help", callback_data="HELP"),
        InlineKeyboardButton(text="Close", callback_data="CLOSE"),
    ],
]

ABOUT_BTN = [
    [
        InlineKeyboardButton(text="Support", url=f"https://t.me/{_support()}"),
        InlineKeyboardButton(text="Help", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="Owner", user_id=_owner_id() if _owner_id() else 777000),
    ],
    [
        InlineKeyboardButton(text="Updates", url=f"https://t.me/{_update()}"),
        InlineKeyboardButton(text="Back", callback_data="BACK"),
    ],
]
