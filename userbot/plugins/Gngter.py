from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("gangster ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**EVERYBODY**")
        await asyncio.sleep(2)
        await event.edit("**IS**")
        await asyncio.sleep(2)
        await event.edit("**GANGSTER**")
        await asyncio.sleep(2)     
        await event.edit("**UNTILL** ")
        await asyncio.sleep(2)
        await event.edit("**@ALONEGANGSTER**")
        await asyncio.sleep(2)
        await event.edit("**ARIVE**")
        await asyncio.sleep(2)
        await event.edit("😏😏")
        await asyncio.sleep(2)
        await event.edit("**EVERYONE  IS  GANGSTER \n  UNTILL  @ALONEGANGSTER  ARRIVE** 🔥🔥🔥")
