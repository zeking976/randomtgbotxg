#!/usr/bin/env python3
import asyncio
import os
import random
from dotenv import load_dotenv
from telegram import Bot

# Load environment variables from t.env
load_dotenv("t.env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_CHANNEL_ID = os.getenv("TARGET_CHANNEL_ID")

bot = Bot(token=BOT_TOKEN)

RANDOM_MESSAGES = [
    "Hello from the bot!",
    "Automated message check.",
    "System heartbeat: OK",
    "Random ping.",
    "Another message from the loop.",
    "This is a test message.",
]

async def send_loop():
    while True:
        msg = random.choice(RANDOM_MESSAGES)
        await bot.send_message(chat_id=TARGET_CHANNEL_ID, text=msg)
        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(send_loop())