
import asyncio

from random import choice

from pyrogram import filters, Client
from pyrogram.types import Message

from STORMDB.data import RAID, STORMS
from config import SUDO_USERS


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], ["."]))
async def dmraid(xspam: Client, message: Message):
      kex = message.text.split(" ")

      if len(kex) == 3:
          ok = await xspam.get_users(kex[2])
          id = ok.id

          if id in STORMS:
                await message.reply_text(f"Your The Verified Lanja✅")
          elif id in SUDO_USERS:
                await message.reply_text(f"This Person ni sudo Loki add dhenginam")
          else:
              counts = int(kex[1])
              await message.reply_text("Dm Raid Ayindhi Ra Puka")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.1)

      elif message.reply_to_message and (len(kex) == 2):
          user_id = message.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id

          if id in STORMS:
                await message.reply_text(f"Your The Verified Lanja✅")
          elif id in SUDO_USERS:
                await message.reply_text(f"This Person ni sudo Loki add dhenginam")
          else:
              counts = int(kex[1])
              await message.reply_text("Dm Raid Ayindhi Ra Puka")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.1)

      else:
            await message.reply_text(".ᴅᴍʀᴀɪᴅ 13 <ᴜꜱᴇʀ ɪᴅ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], ["."]))
async def dmspam(client: Client, message: Message):
    kex = message.text.split(" ", 3)

    if  len(kex) == 4:
        uid = int(kex[2])
        if uid in STORMS:
            await message.reply_text(f"Your The Verified Lanja✅")
        elif uid in SUDO_USERS:
            await message.reply_text(f"This Person ni sudo Loki add dhenginam")
        else:
            quantity, spam_text = int(kex[1]), kex[3]
            await message.reply_text("Dm la Dhengulata Successfull ga started")
            for _ in range(quantity):
                await client.send_message(uid, spam_text)
                await asyncio.sleep(0.3)

    elif message.reply_to_message and (len(kex) == 3):
        id = message.reply_to_message.from_user.id

        if id in STORMS:
            await message.reply_text(f"Your The Verified Lanja✅")
        elif id in SUDO_USERS:
            await message.reply_text(f"This Person ni sudo Loki add dhenginam")
        else:
            quantity = int(kex[1])
            spam_text = kex[2]
            await message.reply_text("Dm la Dhengulata Successfull ga started")
            for _ in range(quantity):
                await client.send_message(id, spam_text)
                await asyncio.sleep(0.3)

    else:
        await message.reply_text(".dmspam 13 User Id Reply To User")
