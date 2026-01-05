import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 2040
api_hash = 'b18441a1ff607e10a989891a5462e627'
string_session = os.getenv("SESSION_STRING")

client = TelegramClient(StringSession(string_session), api_id, api_hash)

replied_users = set()

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def handler(event):
    user_id = event.sender_id
    if user_id not in replied_users:
        reply_text = "سلام من افلاین هستم انلاین که شدم جوابتون میدم"
        await asyncio.sleep(2)
        await event.reply(reply_text)
        replied_users.add(user_id)

async def main():
    await client.start()
    print("Bot is running...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
  
