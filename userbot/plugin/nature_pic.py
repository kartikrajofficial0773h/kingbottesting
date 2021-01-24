'''Usage .naturepic
Im Not Responsible For Any Ban caused By This
Owner @Nihinivi'''

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from uniborg.util import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRING = [
  "hd-wallpapers-nature-1080p"
]

async def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile('/\w+/full.+.jpg')
    f = f.findall(pc)
    fy = "http://getwallpapers.com"+random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")
    urllib.request.urlretrieve(fy,"donottouch.jpg")
@borg.on(admin_cmd(pattern="naturepic ?(.*)", allow_sudo=True))
async def main(event):
    await event.reply("**Auto nature pic successfully started**") #Owner @NihiNivi
    while True:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")  
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(60) #Edit this to your required needs
