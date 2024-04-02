import sys
import datetime

from os import execle, environ
from config import ALIVE_PIC, SUDO_USERS

from pyrogram import Client, filters
from pyrogram.types import Message

KEX = f"""ㅤ Iam a UserBot ‌🪽\n
Hey Iam Alive Chief"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], ["."]))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      Fuk = await e.reply("⚡")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 10000
      await Fuk.edit_text(f"ping \n» `{ms} ms`")

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["reboot", "restart"], ["."]))
async def restart_bot(_, message: Message):
    msg = await message.reply("Restarting...")
    args = ["python3", "-m", "STORM"]
    await msg.edit("ʀᴇꜱᴛᴀʀᴛɪɴɢ...")
    os.execv(sys.executable, [sys.executable] + args)     

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], ["."]))
async def alive(xspam: Client, msg: Message):
       if ".jpg" in ALIVE_PIC or ".png" in ALIVE_PIC:
              await xspam.send_photo(msg.chat.id, ALIVE_PIC, caption=KEX)
       if ".mp4" in ALIVE_PIC or ".MP4," in ALIVE_PIC:
              await xspam.send_video(msg.chat.   id, ALIVE_PIC, caption=KEX)    
