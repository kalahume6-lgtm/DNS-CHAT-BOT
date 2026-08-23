from config import OWNER_USERNAME, SUPPORT_GRP

BOT_NAME = "YASHIKA"
BOT_USERNAME = "YASHIKA_CHAT_BOT"

START = """**
{} ᴛʜᴇ ꜱᴜᴘᴇʀғᴀꜱᴛ ᴄʜᴀᴛʙᴏᴛ 💞

➪ ꜱᴜᴘᴏʀᴛꜱ ᴛᴇxᴛ, ꜱᴛɪᴄᴋᴇʀ, ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ...
➪ ᴍᴜʟᴛɪ-ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴇᴀᴄʜ ᴄʜᴀᴛ /lang
➪ ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ/ᴅɪꜱᴀʙʟᴇᴅ ʙʏ /chatbot

๏ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : {}
๏ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ : {}
๏ ᴜᴘᴛɪᴍᴇ » {}

╔═════════╗
║ ➻ ᴍʏ ʀᴇᴘᴏ ➪ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/kalahume6-lgtm/DNS-CHAT-BOT)
║ ➻ ᴄʀᴇᴀᴛᴏʀ ➪ [ᴅɴs ✯ ᴏᴡɴᴇʀ](https://t.me/{})
╚═════════╝
**""".format("{}", "{}", "{}", "{}", OWNER_USERNAME or "KARTIK_NISHAD_3")

# Fix: START me format placeholders sahi rakhe
START = f"""**
{{}} ᴛʜᴇ ꜱᴜᴘᴇʀғᴀꜱᴛ ᴄʜᴀᴛʙᴏᴛ 💞

➪ ꜱᴜᴘᴏʀᴛꜱ ᴛᴇxᴛ, ꜱᴛɪᴄᴋᴇʀ, ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ...
➪ ᴍᴜʟᴛɪ-ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴇᴀᴄʜ ᴄʜᴀᴛ /lang
➪ ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ/ᴅɪꜱᴀʙʟᴇᴅ ʙʏ /chatbot

๏ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : {{}}
๏ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ : {{}}
๏ ᴜᴘᴛɪᴍᴇ » {{}}

╔═════════╗
║ ➻ ᴍʏ ʀᴇᴘᴏ ➪ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/kalahume6-lgtm/DNS-CHAT-BOT)
║ ➻ ᴄʀᴇᴀᴛᴏʀ ➪ [ᴅɴs ✯ ᴏᴡɴᴇʀ](https://t.me/{OWNER_USERNAME or "KARTIK_NISHAD_3"})
╚═════════╝
**"""

HELP_READ = f"""**
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ]({SUPPORT_GRP or "RU_DRA_098"}).

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /**
**"""

ADMIN_READ = f"""**
๏ Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅs ғᴏʀ Gʀᴏᴜᴘ

➻ /chatbot - ᴏɴ/ᴏғғ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ
➻ /lang - sᴇᴛ ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴛʜᴇ ɢʀᴏᴜᴘ
➻ /status - ᴄʜᴇᴄᴋ ᴄʜᴀᴛʙᴏᴛ sᴛᴀᴛᴜs
──────────────
๏ ᴏɴʟʏ Aᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs
**"""

# CHATBOT_ON buttons (chatbot.py me use hota hai)
CHATBOT_ON = [
    [
        {"text": "ᴇɴᴀʙʟᴇ", "callback_data": "enable_chatbot"},
        {"text": "ᴅɪsᴀʙʟᴇ", "callback_data": "disable_chatbot"},
    ],
]


def get_tools_data_read():
    from DNSCHAT import DNSCHAT
    return f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {DNSCHAT.mention}:

➻ /start ᴛᴏ ᴡᴀᴋᴇ ᴜᴘ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ʀᴇᴄᴇɪᴠᴇ ᴀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ!
──────────────
➻ /help ғᴏʀ ɢᴇᴛᴛɪɴɢ ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ғᴇᴀᴛᴜʀᴇs.
──────────────
➻ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ (ᴘɪɴɢ) ᴏғ ᴛʜᴇ ʙᴏᴛ!
──────────────
➻ /id ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ, ᴄʜᴀᴛ ɪᴅ, ᴀɴᴅ ᴍᴇssᴀɢᴇ ɪᴅ ᴀʟʟ ɪɴ ᴏɴᴇ ᴍᴇssᴀɢᴇ.
──────────────
➻ /broadcast ᴛᴏ ғᴏʀᴡᴀʀᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄʜᴀᴛs ʙᴀsᴇᴅ ᴏɴ sᴘᴇᴄɪғɪᴇᴅ ғʟᴀɢs!
ᴇxᴀᴍᴘʟᴇ: `/broadcast -user -pin ʜᴇʟʟᴏ ғʀɪᴇɴᴅs`
──────────────
➻ /shayri ɢᴇᴛ ʀᴀɴᴅᴏᴍ sʜᴀʏʀɪ ғᴏʀ ʏᴏᴜʀ ʟᴏᴠᴇ
──────────────
➻ ᴜsᴇ /repo ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ ᴛʜᴇ ʙᴏᴛ!
──────────────
๏ ᴍᴀᴅᴇ ʙʏ ➪ [KARTIK ✯ ᴏᴡɴᴇʀ](https://t.me/{OWNER_USERNAME or "KARTIK_NISHAD_3"}) 💞**
"""


def get_chatbot_read():
    from DNSCHAT import DNSCHAT
    return f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {DNSCHAT.mention}:

➻ /chatbot - ᴏᴘᴇɴs ᴏᴘᴛɪᴏɴs ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.
──────────────
➻ /lang, /language, /setlang - ᴏᴘᴇɴs ᴀ ᴍᴇɴᴜ ᴛᴏ sᴇʟᴇᴄᴛ ᴛʜᴇ ᴄʜᴀᴛ ʟᴀɴɢᴜᴀɢᴇ.
──────────────
➻ /resetlang, /nolang - ʀᴇsᴇᴛs ᴛʜᴇ ʙᴏᴛ's ʟᴀɴɢᴜᴀɢᴇ ᴛᴏ ᴍɪxᴇᴅ ʟᴀɴɢᴜᴀɢᴇ.
──────────────
/status - ᴄʜᴇᴄᴋ ᴄʜᴀᴛʙᴏᴛ ᴀᴄᴛɪᴠᴇ ᴏʀ ɴᴏᴛ.
──────────────
📡 ᴍᴀᴅᴇ ʙʏ ➪ [KARTIK ✯ ᴏᴡɴᴇʀ](https://t.me/{OWNER_USERNAME or "KARTIK_NISHAD_3"}) 💞**
"""


def get_source_read():
    from DNSCHAT import DNSCHAT
    return (
        f"**ʜᴇʏ, ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ [{DNSCHAT.name}](https://t.me/{DNSCHAT.username}) ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.**\n"
        "**ᴘʟᴇᴀsᴇ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ & ɢɪᴠᴇ ᴛʜᴇ sᴛᴀʀ ✯**\n"
        "**──────────────────**\n"
        "**ʜᴇʀᴇ ɪs ᴛʜᴇ [sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ](https://github.com/kalahume6-lgtm/DNS-CHAT-BOT)**\n"
        "**──────────────────**\n"
        f"**ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ]({SUPPORT_GRP or 'RU_DRA_098'}).**\n"
        f"**||📡 ᴍᴀᴅᴇ ʙʏ ➪ [ᴅɴs ✯ ᴏᴡɴᴇʀ](https://t.me/{OWNER_USERNAME or 'RU_DRA_098'}) 💞||**"
    )


# Constant version (repo command ke liye)
SOURCE_READ = (
    "**ʜᴇʏ, ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.**\n"
    "**ᴘʟᴇᴀsᴇ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ & ɢɪᴠᴇ ᴛʜᴇ sᴛᴀʀ ✯**\n"
    "**──────────────────**\n"
    "**ʜᴇʀᴇ ɪs ᴛʜᴇ [sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ](https://github.com/kalahume6-lgtm/DNS-CHAT-BOT)**\n"
    "**──────────────────**\n"
    f"**ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ]({SUPPORT_GRP or 'RU_DRA_098'}).**\n"
    f"**||📡 ᴍᴀᴅᴇ ʙʏ ➪ [ᴅɴs ✯ ᴏᴡɴᴇʀ](https://t.me/{OWNER_USERNAME or 'KARTIK_NISHAD_3}) 💞||**"
)


def get_about_read():
    from DNSCHAT import DNSCHAT
    return f"""**
➻ [{DNSCHAT.name}](https://t.me/{DNSCHAT.username}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.
➻ [{DNSCHAT.name}](https://t.me/{DNSCHAT.username}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.
➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.
➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ
──────────────
➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴘ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{DNSCHAT.name}](https://t.me/{DNSCHAT.username})
**"""
