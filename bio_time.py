import time
import asyncio
from datetime import datetime
from telethon import TelegramClient, functions

api_id = 20912747
api_hash = "9e8edd6ff27d9a49daa846877e6eab50"

client = TelegramClient("my_session", api_id, api_hash)

async def update_bio():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        new_bio = f"دلمگرفتازتبحثلاتینبود!☆ | {current_time}"

        await client(functions.account.UpdateProfileRequest(about=new_bio))
        print(f"✅ Bio updated: {new_bio}")

        await asyncio.sleep(60)

async def main():
    await client.start()
    await update_bio()

with client:
    client.loop.run_until_complete(main())
