import sys
import asyncio
import importlib
import os
import threading
from flask import Flask
from pyrogram import idle, filters, raw
from pyrogram.types import BotCommand, Message
from pyrogram.errors import FloodWait

from config import OWNER_ID
from DNSCHAT import LOGGER, DNSCHAT
from DNSCHAT.modules import ALL_MODULES


async def anony_boot():
    # Modules pehle load
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("DNSCHAT.modules." + all_module)
            LOGGER.info(f"Successfully imported : {all_module}")
        except Exception as e:
            LOGGER.error(f"Failed to import {all_module}: {e}")

    # Start bot
    try:
        await DNSCHAT.start()
    except FloodWait as e:
        wait_time = int(e.value)
        LOGGER.error(f"FloodWait: sleeping {wait_time}s...")
        await asyncio.sleep(wait_time + 5)
        await DNSCHAT.start()
    except Exception as ex:
        LOGGER.error(f"Start failed: {ex}")
        sys.exit(1)

    LOGGER.info(f"Bot Started as {DNSCHAT.name}")

    # IMPORTANT: purana webhook hatao taaki polling chale
    try:
        await DNSCHAT.invoke(
            raw.functions.bots.DeleteWebhook(drop_pending_updates=True)
        )
        LOGGER.info("Webhook deleted (if any). Polling active.")
    except Exception as e:
        LOGGER.info(f"delete_webhook info: {e}")

    # Catch-all: koi bhi message aaye to log + /test reply
    @DNSCHAT.on_message()
    async def debug_all(client, message: Message):
        text = message.text or message.caption or ""
        uid = message.from_user.id if message.from_user else "unknown"
        LOGGER.info(f"GOT UPDATE from {uid}: {text[:80]}")

        if text.startswith("/test"):
            await message.reply_text("Test OK - bot is receiving your messages!")
        elif text.startswith("/start"):
            await message.reply_text(
                f"Hello {message.from_user.mention}!\n"
                f"Bot is working.\n"
                f"Try /test /help /ping /repo"
            )

    try:
        await DNSCHAT.set_bot_commands(
            commands=[
                BotCommand("start", "Start the bot"),
                BotCommand("test", "Test reply"),
                BotCommand("help", "Help"),
                BotCommand("ping", "Ping"),
                BotCommand("repo", "Source"),
                BotCommand("stats", "Stats"),
                BotCommand("id", "IDs"),
                BotCommand("chatbot", "Chatbot on/off"),
                BotCommand("lang", "Language"),
                BotCommand("shayri", "Shayri"),
            ]
        )
        LOGGER.info("Bot commands set successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to set bot commands: {ex}")

    LOGGER.info(f"@{DNSCHAT.username} Started. Waiting for messages...")

    if OWNER_ID:
        try:
            await DNSCHAT.send_message(
                int(OWNER_ID),
                f"{DNSCHAT.mention} started.\nSend /test now",
            )
        except Exception as e:
            LOGGER.info(f"Owner notify failed: {e}")

    await idle()


app = Flask(__name__)


@app.route("/")
def home():
    return "DNS CHAT BOT is running"


@app.route("/health")
def health():
    return "OK", 200


def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    LOGGER.info(f"Health check on port {os.environ.get('PORT', 10000)}")
    asyncio.run(anony_boot())
