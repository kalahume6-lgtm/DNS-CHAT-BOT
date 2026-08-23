import sys
import asyncio
import importlib
import os
from flask import Flask
import threading
from pyrogram import idle
from pyrogram.types import BotCommand
from pyrogram.errors import FloodWait
from config import OWNER_ID
from DNSCHAT import LOGGER, DNSCHAT
from DNSCHAT.modules import ALL_MODULES


async def anony_boot():
    max_retries = 3
    for attempt in range(max_retries):
        try:
            await DNSCHAT.start()
            break
        except FloodWait as e:
            wait_time = int(e.value)
            LOGGER.error(
                f"FloodWait received. Sleeping {wait_time} seconds "
                f"(attempt {attempt + 1}/{max_retries})..."
            )
            # Sleep in chunks so process stays alive
            remaining = wait_time + 10
            while remaining > 0:
                sleep_for = min(60, remaining)
                await asyncio.sleep(sleep_for)
                remaining -= sleep_for
                LOGGER.info(f"FloodWait: {remaining} seconds left...")
        except Exception as ex:
            LOGGER.error(f"Start failed: {ex}")
            if attempt == max_retries - 1:
                sys.exit(1)
            await asyncio.sleep(30)
    else:
        LOGGER.error("Could not start bot after retries")
        sys.exit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("DNSCHAT.modules." + all_module)
        LOGGER.info(f"Successfully imported : {all_module}")

    try:
        await DNSCHAT.set_bot_commands(
            commands=[
                BotCommand("start", "Start the bot"),
                BotCommand("help", "Get the help menu"),
                BotCommand("ping", "Check if the bot is alive or dead"),
                BotCommand("lang", "Select bot reply language"),
                BotCommand("resetlang", "Reset to default bot reply lang"),
                BotCommand("id", "Get users user_id"),
                BotCommand("stats", "Check bot stats"),
                BotCommand("gcast", "Broadcast any message to groups/users"),
                BotCommand("chatbot", "Enable or disable chatbot"),
                BotCommand("status", "Check chatbot enable or disable in chat"),
                BotCommand("shayri", "Get random shayri for love"),
                BotCommand("repo", "Get chatbot source code"),
            ]
        )
        LOGGER.info("Bot commands set successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to set bot commands: {ex}")

    LOGGER.info(f"@{DNSCHAT.username} Started.")

    if OWNER_ID:
        try:
            await DNSCHAT.send_message(OWNER_ID, f"{DNSCHAT.mention} has started")
        except Exception:
            LOGGER.info(f"@{DNSCHAT.username} Started, please start the bot from owner id.")
    else:
        LOGGER.warning("OWNER_ID not set. Skipping start notification.")

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
