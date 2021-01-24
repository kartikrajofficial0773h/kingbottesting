""" Speak a line... 
    Command .mirzapur
    By @The_Avengers_leader """

from telethon import events
import asyncio
import os
import sys
import random
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"mirzapur$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("speak a line.......")
    await asyncio.sleep(2)
    x=(random.randrange(1,19))
    if x==1:
        await event.edit("Neta banna hai toh gundey paalo. Gundey math bano**")
    if x==2:
        await event.edit("Darr ki yahi dikkat hain, ki kabhi bhi Khatam ho sakta hai")
    if x==3:
        await event.edit("‘Mata ji yahan hai, Behen yaha hai, Maa-Behen ek karne mein aasani hogi’ – Munna Bhaiya ")
    if x==4:
        await event.edit("Guns ki maddad se darr nahi badhana hai, darr ki maddad se guns badhani hai")
    if x==5:
       await  event.edit("“Suru majburi mein kiye the…..Ab maza aa rahe hain”") 
    if x==6:
        await event.edit("“Har bar garam karke Thanda hi chhod dete ho. Tumhare chutiyape kab kahtam hogen” ")
    if x==7:
        await event.edit("Izzat nahi karte hain...darte hain sab")
    if x==8:
        await event.edit("Gun se hamein tension hai hain....bachpan se dekhe hain ")
    if x==9:
        await event.edit("Saale Horn gaan* mein daal degen abhi....Po..Po...helicoptor ban jagoge")
    if x==10:
        await event.edit("“When the snows fall, and the white winds blow, the lone wolf dies, but the pack survives.” ")
    if x==11:
        await event.edit("kaise chutar matka rahe hai sale chutiye!! ")
    if x==12:
        await event.edit("nacho,bsdk,nacho")
    if x==13:
        await event.edit("to tum bsdk iske liye tum mere darwaje pe chale aaye!! ")
    if x==14:
        await event.edit("majak bana rakah hai madarchod!! ")
    if x==15:
        await event.edit("jinda to jhaat ke ball bhi hai!! ")
    if x==16:
        await event.edit("are tum itni choti si baat pe hah diye!! ")
    if x==17:
        await event.edit("Privacy is a Myth, just like Democracy ")
    if x==18:
        await event.edit("Yeh Mumbai hai, yaha ghar ke naam pe kya milta hai? Machis ki dibbi, tilli jaise pade raho iske andar.")
    if x==19:
        await event.edit("Written and Created By: @The_Avengers_leader join @pyfilestonystark ! thank you🙏🏻❤")
