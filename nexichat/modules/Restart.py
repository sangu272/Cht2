import os
import shutil
import asyncio
from pyrogram.types import BotCommand
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import filters, Client
from nexichat import nexichat
from config import OWNER_ID

@nexichat.on_message(
    filters.command(["restart"]) & filters.user(int(OWNER_ID))
)
async def restart(client: Client, message: Message):
    reply = await message.reply_text("**🔁 Rᴇsᴛᴀʀᴛɪɴɢ 🔥 ...**")
    await message.delete()
    await reply.edit_text("🥀 SᴜᴄᴄᴇssFᴜʟʟʏ RᴇSᴛᴀʀᴛᴇᴅ\n ︎ᴄʜᴀᴛʙᴏᴛ  🔥 ...\n\n💕 Pʟᴇᴀsᴇ Wᴀɪᴛ 1-2 MɪN Fᴏʀ\nLᴏᴀᴅ Usᴇʀ Pʟᴜɢɪɴs ✨ ...</b>")
    os.system(f"kill -9 {os.getpid()} && python3 -m nexichat")
  
