""" Speak a flirting line... 
    Command .flirt
    By @The_Avengers_leader """

from telethon import events
import asyncio
import os
import sys
import random
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"flirt$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("speaking truth about u.......")
    await asyncio.sleep(2)
    x=(random.randrange(1,25))
    if x==1:
        await event.edit("They say Disneyland is the happiest place on earth. Well apparently, no one has ever been standing next to you! **")
    if x==2:
        await event.edit("For some reason, I was feeling a little off today. But when you came along, you ")
    if x==3:
        await event.edit("Is there an airport nearby or is it my heart taking off? ")
    if x==4:
        await event.edit("Was your dad a boxer? Because damn, you’re a knockout!")
    if x==5:
       await event.edit("I was wondering if you had an extra heart. Mine was just stolen. ") 
    if x==6:
        await event.edit("Did the sun come out or did you just smile at me? ")
    if x==7:
        await event.edit("Kiss me if I’m wrong, but dinosaurs still exist, right? ")
    if x==8:
        await event.edit("Hey, you’re pretty and I’m cute. Together we’d be Pretty Cute. ")
    if x==9:
        await event.edit("Is your name Google? Because you have everything I’ve been searching for. ")
    if x==10:
        await event.edit("There must be something wrong with my eyes, I can’t take them off you.")
    if x==11:
        await event.edit("I’m sorry, were you talking to me? [No] Well then, please start. ")
    if x==12:
        await event.edit("Was you father an alien? Because there’s nothing else like you on Earth! ")
    if x==13:
        await event.edit("Was your father a thief? ‘Cause someone stole the stars from the sky and put them in your eyess ")
    if x==14:
        await event.edit("Do you have a pencil? Cause I want to erase your past and write our future. ")
    if x==15:
        await event.edit(" Can you take me to the doctor? Because I just broke my leg falling for you. ")
    if x==16:
        await event.edit("You don’t need keys to drive me crazy.")
    if x==17:
        await event.edit("Sorry, but you owe me a drink. [Why?] Because when I looked at you, I dropped mine.")
    if x==18:
       await event.edit("You must be a broom, ‘cause you just swept me off my feet. ")
    if x==19:
        await event.edit("Have you been to the doctor’s lately? Cause I think you’re lacking some vitamin me.")
    if x==20:
        await event.edit("Nice shirt! What’s it made out of, boyfriend material? ")
    if x==21:
        await event.edit("I’m lost. Can you give me directions to your heart? ")
    if x==22:
        await event.edit("If I’m vinegar, then you must be baking soda. Because you make me feel all bubbly inside!")
    if x==23:
        await event.edit("Can I follow you home? Cause my parents always told me to follow my dreams. ")
    if x==24:
        await event.edit("Can I borrow a kiss? I swear I’ll give it back. ")
    if x==25:
        await event.edit("Written and Created By: @The_Avengers_leader join @pyfilestonystark ! thank you🙏🏻❤")

 
