"""Fun pligon...for HardcoreUserbot
\nCode by @Kraken_The_BadASS
type .nacho to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="nacho ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Aandd Maand")
        await asyncio.sleep(2)
        await event.edit("Kaa Doola Toola")
        await asyncio.sleep(2)
        await event.edit("Jo naa nacha")
        await asyncio.sleep(2)
        await event.edit("Behen Daa Loda")
        await asyncio.sleep(2)
        await event.edit("Ooe Nacho Bhenchod")
        await asyncio.sleep(2)
        await event.edit("**Aand mand ka doola toola jo na nacha behen da loda... Nach na lawde**")
