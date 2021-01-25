#Credit To @The_Avengers_leader  . copying this is a serious crime which will lead to id ban.


import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="girl ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(" `Dear girls, my father didn,t fucked you mother so don,t call me bhai!\n")
