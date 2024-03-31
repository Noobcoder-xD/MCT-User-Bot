import asyncio

from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from basic import edit_or_reply

from .help import *


@Client.on_message(
    filters.command(["screenshot", "ss"], ".") & filters.private & filters.me
)
async def screenshot(bot: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        bot.invoke(
            functions.messages.SendScreenshotNotification(
                peer=await X.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=X.rnd_id(),
            )
        ),
    )


