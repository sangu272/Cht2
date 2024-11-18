import asyncio
from os import getenv
from config import OWNER_ID
from dotenv import load_dotenv
from pyrogram import Client
import config


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="BADAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=False,
            plugins=dict(root="nexichat.user"),
        )
        

    async def start(self):
        print(f"ꜱᴛᴀʀᴛɪɴɢ ɪᴅ ᴄʜᴀᴛʙᴏᴛ...")

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("TG_BIO_STYLE")
                await self.one.join_chat("TG_BIO_STYLE")
                await self.one.join_chat("ll_ITZ_NAWAB_HERE_ll ")
                await self.one.join_chat("ll_ITZ_NAWAB_HERE_ll")

            except:
                pass

            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
     
            print(f"ɪᴅ-ᴄʜᴀᴛʙᴏᴛ ꜱᴛᴀʀᴛᴇᴅ ᴀꜱ {self.one.me.first_name}")
            
        

    async def stop(self):
        LOGGER(__name__).info(f"ꜱᴛᴏᴘᴘɪɴɢ ɪᴅ-ᴄʜᴀᴛʙᴏᴛ...")
        try:
            if config.STRING1:
                await self.one.stop()
        except:
            pass
