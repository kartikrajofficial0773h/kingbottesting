#Credit To @Hell0ji123b0t . copying this is a serious crime which will lead to id ban.


import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="dad ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(" `IF yOu ArE bAd. tHeN cAlL mE yOuR dAd!\n")
