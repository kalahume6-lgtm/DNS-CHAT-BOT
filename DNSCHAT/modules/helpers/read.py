from config import OWNER_USERNAME, SUPPORT_GRP
from pyrogram import Client, filters

BOT_NAME = "YASHIKA"  
BOT_USERNAME = "YASHIKA_CHAT_BOT"  

START = f"""**..."""
START = f"""**
{{}} ᴛʜᴇ ꜱᴜᴘᴇʀғᴀꜱᴛ ᴄʜᴀᴛʙᴏᴛ 💞

➪ ꜱᴜᴘᴏʀᴛꜱ ᴛᴇxᴛ, ꜱᴛɪᴄᴋᴇʀ, ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ...
➪ ᴍᴜʟᴛɪ-ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴇᴀᴄʜ ᴄʜᴀᴛ /lang
➪ ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ/ᴅɪꜱᴀʙʟᴇᴅ ʙʏ /chatbot

๏ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : {{}}
๏ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ : {{}}
๏ ᴜᴘᴛɪᴍᴇ » {{}}

╔═════════╗
║ ➻ ᴍʏ ʀᴇᴘᴏ ➪ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/RU_DRA_098)  
║ ➻ ᴄʀᴇᴀᴛᴏʀ ➪ [ᴅɴs ✯ ᴏᴡɴᴇʀ](https://t.me/RU_DRA_65)                         
╚═════════╝
**"""

HELP_READ = f"""**
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴏʀᴛ ᴄʜᴀᴛ]({SUPPORT_GRP}).

Aʟ ᴄᴏᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /**
"""

ADMIN_READ = f"""**
๏ Aᴅᴍɪɴ Cᴏᴍᴀɴᴅs ғᴏʀ Gʀᴏᴜᴘ

➻ /chatbot - ᴏɴ/ᴏғғ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ
➻ /lang - sᴇᴛ ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴛʜᴇ ɢʀᴏᴜᴘ
➻ /status - ᴄʜᴇᴄᴋ ᴄʜᴀᴛʙᴏᴛ sᴛᴀᴛᴜs
──────────────
๏ ᴏɴʟʏ Aᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs
**"""

def get_tools_data_read():
    from DNSCHAT import DNSCHAT  # <- Function ke andar import kiya
    return f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴀɴᴅs ғᴏʀ {DNSCHAT.mention}:

➻ /start ᴛᴏ ᴡᴀᴋᴇ ᴜᴘ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ʀᴇᴄᴇɪᴠᴇ ᴀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ!
──────────────
➻ /help ғᴏʀ ɢᴇᴛɪɴɢ ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ᴀʟʟ ᴄᴏᴍᴀɴᴅs ᴀɴᴅ ғᴇᴀᴛᴜʀᴇs.
──────────────
➻ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ (ᴘɪɴɢ) ᴏғ ᴛʜᴇ ʙᴏᴛ!
──────────────
➻ /id ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ, ᴄʜᴀᴛ ɪᴅ, ᴀɴᴅ ᴍᴇssᴀɢᴇ ɪᴅ ᴀʟ ɪɴ ᴏɴᴇ ᴍᴇssᴀɢᴇ.
──────────────
➻ /broadcast ᴛᴏ ғᴏʀᴡᴀʀᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄʜᴀᴛs ʙᴀsᴇᴅ ᴏɴ sᴘᴇᴄɪғɪᴇᴅ ғʟᴀɢs!
ᴇxᴀᴍᴘʟᴇ: `/broadcast -user -pin ʜᴇʟʟᴏ ғʀɪᴇɴᴅs`
──────────────
➻ /shayri ɢᴇᴛ ʀᴀɴᴅᴏᴍ sʜᴀʏʀɪ ғᴏʀ ʏᴏᴜʀ ʟᴏᴠᴇ
──────────────
➻ ᴜsᴇ /repo ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ ᴛʜᴇ ʙᴏᴛ!
──────────────
๏ ᴍᴀᴅᴇ ʙʏ ➪ [KARTIK ✯ ᴏᴡɴᴇʀ](https://t.me/{OWNER_USERNAME}) 💞**
"""

def get_chatbot_read():
    from DNSCHAT import DNSCHAT  # <- Function ke andar import kiya
    return f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴀɴᴅs ғᴏʀ {DNSCHAT.mention}:

➻ /chatbot - ᴏᴘᴇɴs ᴏᴘᴛɪᴏɴs ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.
──────────────
➻ /lang, /language, /setlang - ᴏᴘᴇɴs ᴀ ᴍᴇɴᴜ ᴛᴏ sᴇʟᴇᴄᴛ ᴛʜᴇ ᴄʜᴀᴛ ʟᴀɴɢᴜᴀɢᴇ.  
──────────────
➻ /resetlang, /nolang - ʀᴇsᴇᴛs ᴛʜᴇ ʙᴏᴛ's ʟᴀɴɢᴜᴀɢᴇ ᴛᴏ ᴍɪxᴇᴅ ʟᴀɴɢᴜᴀɢᴇ.
──────────────
/status - ᴄʜᴇᴄᴋ ᴄʜᴀᴛʙᴏᴛ ᴀᴄᴛɪᴠᴇ ᴏʀ ɴᴏᴛ.
──────────────
📡 ᴍᴀᴅᴇ ʙʏ ➪ [KARTIK ✯ ᴏᴡɴᴇʀ](https://t.me/{OWNER_USERNAME}) 💞**
"""

def get_source_read():
    from DNSCHAT import DNSCHAT  # <- Function ke andar import kiya
    return (
        f"**ʜᴇʏ, ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ [{DNSCHAT.name}](https://t.me/{DNSCHAT.username}) ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.**\n"
        "**ᴘʟᴇᴀsᴇ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ & ɢɪᴠᴇ ᴛʜᴇ sᴛᴀʀ ✯**\n"
        "**──────────────────**\n"
        "**ʜᴇʀᴇ ɪs ᴛʜᴇ [sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ](https://github.com/your-repo)**\n"  # Yaha apna repo link daal dena
        "**──────────────────**\n"
        f"**ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ]({SUPPORT_GRP}).**\n"
        f"**||📡 ᴍᴀᴅᴇ ʙʏ ➪ [ᴅɴs ✯ ᴏᴡɴᴇʀ](https://t.me/{OWNER_USERNAME}) 💞||**"
    )

def get_about_read():
    from DNSCHAT import DNSCHAT  # <- Function ke andar import kiya
    return f"""**
➻ [{DNSCHAT.name}](https://t.me/{DNSCHAT.username}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.
➻ [{DNSCHAT.name}](https://t.me/{DNSCHAT.username}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.
➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.
➻ ᴡʀɪᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ
──────────────
➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{DNSCHAT.name}](https://t.me/{DNSCHAT.username})
**"""
