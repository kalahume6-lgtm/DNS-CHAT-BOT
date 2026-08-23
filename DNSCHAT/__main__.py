import sys
import asyncio
import importlib
import os
import threading
from flask import Flask
from pyrogram import idle, filters
from pyrogram.types import BotCommand, Message
from pyrogram.errors import FloodWait

from config import OWNER_ID
from DNSCHAT import LOGGER, DNSCHAT
from DNSCHAT.modules import ALL_MODULES


async def anony_boot():
    # 1) Pehle saare modules load karo (handlers register honge)
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("DNSCHAT.modules." + all_module)
            LOGGER.info(f"Successfully imported : {all_module}")
        except Exception as e:
            LOGGER.error(f"Failed to import {all_module}: {e}")

    # 2) Test handler - seedha main me (debug ke liye)
    @DNSCHAT.on_message(filters.command("test"))
    async def test_cmd(client, message: Message):
        await message.reply_text("Test OK - bot is receiving messages!")

    @DNSCHAT.on_message(filters.text & filters.private & filters.command("start"))
    async def force_start(client, message: Message):
        await message.reply_text(
            f"Hello {message.from_user.mention}!\n"
            f"Bot is working.\n"
            f"Try /test /ping /help /repo"
        )

    # 3) Ab bot start karo
    try:
        await DNSCHAT.start()
    except FloodWait as e:
        wait_time = int(e.value)
        LOGGER.error(f"FloodWait: sleeping {wait_time} seconds...")
        remaining = wait_time + 10
        while remaining > 0:
            sleep_for = min(60, remaining)
            await asyncio.sleep(sleep_for)
            remaining -= sleep_for
            LOGGER.info(f"FloodWait: {remaining} seconds left...")
        await DNSCHAT.start()
    except Exception as ex:
        LOGGER.error(f"Start failed: {ex}")
        sys.exit(1)

    LOGGER.info(f"Bot Started as {DNSCHAT.name}")

    try:
        await DNSCHAT.set_bot_commands(
            commands=[
                BotCommand("start", "Start the bot"),
                BotCommand("help", "Help menu"),
                BotCommand("ping", "Ping"),
                BotCommand("test", "Test reply"),
                BotCommand("repo", "Source code"),
                BotCommand("stats", "Stats"),
                BotCommand("id", "Get IDs"),
                BotCommand("chatbot", "Enable/disable chatbot"),
                BotCommand("lang", "Language"),
                BotCommand("shayri", "Random shayri"),
            ]
        )
        LOGGER.info("Bot commands set successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to set bot commands: {ex}")

    LOGGER.info(f"@{DNSCHAT.username} Started.")

    if OWNER_ID:
        try:
            await DNSCHAT.send_message(
                int(OWNER_ID),
                f"{DNSCHAT.mention} has started\nSend /test to check replies",
            )
        except Exception as e:
            LOGGER.info(f"Could not notify owner: {e}")

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
    LOGGER.info(f"Health check server started on port {os.environ.get('PORT', 10000)}")

    asyncio.run(anony_boot())
    LOGGER.info("Stopping DNSCHAT Bot...")
