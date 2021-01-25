""" Speak a flirting line... 
    Command .bflirt
    By @The_Avengers_leader """

from telethon import events
import asyncio
import os
import sys
import random
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"bflirt$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("speaking truth about u.......")
    await asyncio.sleep(2)
    x=(random.randrange(1,25))
    if x==1:
        await event.edit("Just so you know, my lips won’t just kiss themselves.**")
    if x==2:
        await event.edit("I’m sorry, your shirt has to go. However, you can stay as long as you please.")
    if x==3:
        await event.edit("Can I slap you in the face...with my lips? ")
    if x==4:
        await event.edit("You have a bit of cute on your face.")
    if x==5:
     await event.edit("Your lips are kind of wrinkled. Mind if I press them?") 
    if x==6:
       await event.edit("That shirt looks great on you! As a matter of fact, so would I.")
    if x==7:
      await event.edit("Why do you have to look so good?! I can’t concentrate on what I’m doing!")
    if x==8:
        await event.edit("I will report you to the police for stealing my heart!")
    if x==9:
        await event.edit("Wait a second. I need to breathe. Being with you takes my breath away.")
    if x==10:
        await event.edit("I like you just how I like my coffee: tall, dark and strong.")
    if x==11:
        await event.edit("You seem familiar. You look a lot like my future boyfriend/husband. ")
    if x==12:
        await event.edit("Your lips are meant to be kissed. Let’s not waste them. ")
    if x==13:
        await event.edit("I was feeling OFF the whole day. But then, you showed up and turned me ON!")
    if x==14:
        await event.edit("Hey, please keep your distance. I might fall for you any time. ")
    if x==15:
        await event.edit("You remind me of a magnet because you are attracting me to you.  ")
    if x==16:
        await event.edit("I don't know what you think of me, but I hope it's X-rated.")
    if x==17:
        await event.edit("Your face would make a great throne for a queen like me.")
    if x==18:
       await event.edit("You have been such a naughty boy. Go to my bedroom!")
    if x==19:
        await event.edit("My hands feel cold. Can I put them in your pants to warm up?")
    if x==20:
        await event.edit("Are you a candle? Because I want to blow you.")
    if x==21:
        await event.edit("Are you a burger patty? Because you can be the meat between my buns. ")
    if x==22:
        await event.edit("You seem like a hard worker. I’ve got an opening you can fill.")
    if x==23:
        await event.edit("Your lap seems available. Can I sit on it? ")
    if x==24:
        await event.edit("You’re like hot chocolate and I’m like marshmallows. You're hot and I want be on top of you. ")
    if x==25:
        await event.edit("Written and Created By: @The_Avengers_leader join @pyfilestonystark ! thank you🙏🏻❤")
