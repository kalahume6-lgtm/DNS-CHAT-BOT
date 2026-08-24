from config import OWNER_USERNAME, SUPPORT_GRP

_owner = OWNER_USERNAME or "KARTIK_NISHAD_3"
_support = SUPPORT_GRP or "RU_DRA_098"

START = (
    "**"
    "{} ᴛʜᴇ ꜱᴜᴘᴇʀғᴀꜱᴛ ᴄʜᴀᴛʙᴏᴛ 💞\n\n"
    "➪ ꜱᴜᴘᴘᴏʀᴛꜱ ᴛᴇxᴛ, ꜱᴛɪᴄᴋᴇʀ, ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ...\n"
    "➪ ᴍᴜʟᴛɪ-ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴇᴀᴄʜ ᴄʜᴀᴛ /lang\n"
    "➪ ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ/ᴅɪꜱᴀʙʟᴇᴅ ʙʏ /chatbot\n\n"
    "๏ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : {}\n"
    "๏ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ : {}\n"
    "๏ ᴜᴘᴛɪᴍᴇ » {}\n\n"
    "╔═════════╗\n"
    "║ ➻ ᴍʏ ʀᴇᴘᴏ ➪ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/kalahume6-lgtm/DNS-CHAT-BOT)\n"
    f"║ ➻ ᴄʀᴇᴀᴛᴏʀ ➪ [ᴅɴs ✯ ᴏᴡɴᴇʀ](https://t.me/{_owner})\n"
    "╚═════════╝\n"
    "**"
)

HELP_READ = (
    "**\n"
    "Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  "
    f"Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ]({_support}).\n\n"
    "Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /**\n"
    "**"
)

ADMIN_READ = (
    "**\n"
    "๏ Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅs ғᴏʀ Gʀᴏᴜᴘ\n\n"
    "➻ /chatbot - ᴏɴ/ᴏғғ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ\n"
    "➻ /lang - sᴇᴛ ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴛʜᴇ ɢʀᴏᴜᴘ\n"
    "➻ /status - ᴄʜᴇᴄᴋ ᴄʜᴀᴛʙᴏᴛ sᴛᴀᴛᴜs\n"
    "──────────────\n"
    "๏ ᴏɴʟʏ Aᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs\n"
    "**"
)

SOURCE_READ = (
    "**ʜᴇʏ, ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.**\n"
    "**ᴘʟᴇᴀsᴇ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ & ɢɪᴠᴇ ᴛʜᴇ sᴛᴀʀ ✯**\n"
    "**──────────────────**\n"
    "**ʜᴇʀᴇ ɪs ᴛʜᴇ [sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ](https://github.com/kalahume6-lgtm/DNS-CHAT-BOT)**\n"
    "**──────────────────**\n"
    f"**ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ]({_support}).**\n"
    f"**||📡 ᴍᴀᴅᴇ ʙʏ ➪ [ᴅɴs ✯ ᴏᴡɴᴇʀ](https://t.me/{_owner}) 💞||**"
)


def get_tools_data_read():
    from DNSCHAT import DNSCHAT
    return (
        f"**\n"
        f"๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {DNSCHAT.mention}:\n\n"
        "➻ /start ᴛᴏ ᴡᴀᴋᴇ ᴜᴘ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ʀᴇᴄᴇɪᴠᴇ ᴀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ!\n"
        "──────────────\n"
        "➻ /help ғᴏʀ ɢᴇᴛᴛɪɴɢ ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ғᴇᴀᴛᴜʀᴇs.\n"
        "──────────────\n"
        "➻ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ (ᴘɪɴɢ) ᴏғ ᴛʜᴇ ʙᴏᴛ!\n"
        "──────────────\n"
        "➻ /id ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ, ᴄʜᴀᴛ ɪᴅ, ᴀɴᴅ ᴍᴇssᴀɢᴇ ɪᴅ ᴀʟʟ ɪɴ ᴏɴᴇ ᴍᴇssᴀɢᴇ.\n"
        "──────────────\n"
        "➻ /broadcast ᴛᴏ ғᴏʀᴡᴀʀᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄʜᴀᴛs ʙᴀsᴇᴅ ᴏɴ sᴘᴇᴄɪғɪᴇᴅ ғʟᴀɢs!\n"
        "ᴇxᴀᴍᴘʟᴇ: `/broadcast -user -pin ʜᴇʟʟᴏ ғʀɪᴇɴᴅs`\n"
        "──────────────\n"
        "➻ /shayri ɢᴇᴛ ʀᴀɴᴅᴏᴍ sʜᴀʏʀɪ ғᴏʀ ʏᴏᴜʀ ʟᴏᴠᴇ\n"
        "──────────────\n"
        "➻ ᴜsᴇ /repo ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ ᴛʜᴇ ʙᴏᴛ!\n"
        "──────────────\n"
        f"๏ ᴍᴀᴅᴇ ʙʏ ➪ [KARTIK ✯ ᴏᴡɴᴇʀ](https://t.me/{_owner}) 💞**"
    )


def get_chatbot_read():
    from DNSCHAT import DNSCHAT
    return (
        f"**\n"
        f"๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {DNSCHAT.mention}:\n\n"
        "➻ /chatbot - ᴏᴘᴇɴs ᴏᴘᴛɪᴏɴs ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.\n"
        "──────────────\n"
        "➻ /lang, /language, /setlang - ᴏᴘᴇɴs ᴀ ᴍᴇɴᴜ ᴛᴏ sᴇʟᴇᴄᴛ ᴛʜᴇ ᴄʜᴀᴛ ʟᴀɴɢᴜᴀɢᴇ.\n"
        "──────────────\n"
        "➻ /resetlang, /nolang - ʀᴇsᴇᴛs ᴛʜᴇ ʙᴏᴛ's ʟᴀɴɢᴜᴀɢᴇ ᴛᴏ ᴍɪxᴇᴅ ʟᴀɴɢᴜᴀɢᴇ.\n"
        "──────────────\n"
        "/status - ᴄʜᴇᴄᴋ ᴄʜᴀᴛʙᴏᴛ ᴀᴄᴛɪᴠᴇ ᴏʀ ɴᴏᴛ.\n"
        "──────────────\n"
        f"📡 ᴍᴀᴅᴇ ʙʏ ➪ [KARTIK ✯ ᴏᴡɴᴇʀ](https://t.me/{_owner}) 💞**"
    )


def get_source_read():
    from DNSCHAT import DNSCHAT
    return (
        f"**ʜᴇʏ, ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ [{DNSCHAT.name}](https://t.me/{DNSCHAT.username}) ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.**\n"
        "**ᴘʟᴇᴀsᴇ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ & ɢɪᴠᴇ ᴛʜᴇ sᴛᴀʀ ✯**\n"
        "**──────────────────**\n"
        "**ʜᴇʀᴇ ɪs ᴛʜᴇ [sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ](https://github.com/kalahume6-lgtm/DNS-CHAT-BOT)**\n"
        "**──────────────────**\n"
        f"**ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ]({_support}).**\n"
        f"**||📡 ᴍᴀᴅᴇ ʙʏ ➪ [ᴅɴs ✯ ᴏᴡɴᴇʀ](https://t.me/{_owner}) 💞||**"
    )


def get_about_read():
    from DNSCHAT import DNSCHAT
    return (
        f"**\n"
        f"➻ [{DNSCHAT.name}](https://t.me/{DNSCHAT.username}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.\n"
        f"➻ [{DNSCHAT.name}](https://t.me/{DNSCHAT.username}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.\n"
        "➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.\n"
        "➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ\n"
        "──────────────\n"
        f"➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴘ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{DNSCHAT.name}](https://t.me/{DNSCHAT.username})\n"
        "**"
    )
