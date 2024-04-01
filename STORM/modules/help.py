from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

FIRST_TEXT = f"""
✨ **ʙᴏᴛ ʜᴇʟᴘ** ✨

**[⏤͟͟͞͞• 𝐕 𝚫 𝐌 𝐒 𝐈 ˼ㅤㅤ [•ᴧғᴋ•]™](https://t.me/Tg_Moviez_King) ʜᴇʟᴘ ᴍᴇɴᴜ** 🥀

**ʜᴇʟᴘ ᴍᴇɴᴜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ [MCT PRESENTS](https://t.me/MCT_PRESENTS)** ✨

**ᴄʜᴀɴɴᴇʟ: [PVR FILE](https://t.me/PVR_FILE)**
**ꜱᴜᴘᴘᴏʀᴛ: [PVS MOVIES](https://t.me/PVS_MOVIES_UPDATES)**

**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpextra`  
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpspam` 
**» ᴅᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpdm`
**» ʟᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helplove`
**» ꜰᴜɴ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpfun`
**» ɴᴇᴡꜱ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpnews`
**» ᴄᴏɴᴠᴇʀᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpconvert`
**» ɪɴꜰᴏ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpinfo`
**» ᴄʀᴇᴀᴛᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpcreate`
**» ᴘʀᴏꜰɪʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpprofile`
**» ɢᴡɪꜱʜ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpgwish`
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=FIRST_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=FIRST_TEXT)
