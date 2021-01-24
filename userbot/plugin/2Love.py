"""Fun pligon...for HardcoreUserbot
\nCode by @Kraken_The_BadASS
type `.2love` and to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="2love ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Bahte Hue Duriya Ko Kya Modega Koi")
        await asyncio.sleep(2.5)
        await event.edit("Toote Hue Shishe Ko Kya Jodega Koi")
        await asyncio.sleep(2.5)
        await event.edit("Chalo Fir Se Dil Lagake Dekhte Hai")
        await asyncio.sleep(2.5)
        await event.edit("Ab Is Toote Hue Dil Ko Kya Todega Koi")
        await asyncio.sleep(2.5)
        await event.edit("**Bahte Hue Duriya Ko Kya Modega Koi. Toote Hue Shishe Ko Kya Jodega Koi. Chalo Fir Se Dil Lagake Dekhte Hai. Ab Is Toote Hue Dil Ko Kya Todega Koi**")





