import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot


PHOTO = [
    "https://te.legra.ph/file/5481b59e4a31fca4499fe.jpg",
    "https://te.legra.ph/file/85a67867942ff92c5622b.jpg",
    "https://te.legra.ph/file/7a81bab81fb73527b2ad3.jpg",
    "https://te.legra.ph/file/66091a9f4514e8b626ac5.jpg",
    "https://te.legra.ph/file/be5d28bb10a47ce8e6060.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ ᴀɢᴏʀᴀ ʙᴏᴛ​~🕉️**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [Λ𝖦ՕᏒΛ](https://t.me/mr_agora)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/agora_robot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/karunada_kings_and_queens")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod
