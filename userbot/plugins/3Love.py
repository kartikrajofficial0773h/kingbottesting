"""Fun pligon...for HardcoreUserbot
\nCode by @Kraken_The_BadASS
type `.3love` and to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="3love ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Dil Ko Jalate Hai Ham Diye Ki Tarah")
        await asyncio.sleep(2.5)
        await event.edit("Teri Zindagi Main Roshni Lane Ke Liye")
        await asyncio.sleep(2.5)
        await event.edit("Le Lete Hai Har Kaaton Ko Apni Zindagi Mein")
        await asyncio.sleep(2.5)
        await event.edit("Bas Teri Rahon Main Phool Bhichane Ke Liye")
        await asyncio.sleep(2.5)
        await event.edit("**Dil Ko Jalate Hai Ham Diye Ki Tarah,  Teri Zindagi Main Roshni Lane Ke Liye,  Le Lete Hai Har Kaaton Ko Apni Zindagi Mein,  Bas Teri Rahon Main Phool Bhichane Ke Liye**")





