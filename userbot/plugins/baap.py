from telethon import events
import random, re
from uniborg.util import admin_cmd

RUNSREACTS = [
    "TERI MAAAAAAA KAAAAAAAAAA BOXDAAAAA MATARCHODDDDDDDD BAAAP HU TERAAAAAAAAAAAA",
        "`apne lawde ke goli se police ke car mei ghus ke chodunga teri ammy ko hathkadi laga ke kach kach kach jb tak behos na ho jau mai tb !`",
    "TERI MAA KEEEE BOXDE ME PETROL DALKEEEEEE AAAG LGA DUNGAAAAA MADARCHODDDDDDDD TERI MAAAAAAA MUUT NAHI PAEYEGIII",
    "` tak Pelta rahunga  teri 🤣🤣🤣🤣🤣🤣behn ko apna lawde ka malai chataunga roti mei laga ke paros dunga  teri nani ke budhi ch00ton ko aisa baja baja ke lunga na ki uski jawani yaad dila dunga lal kila mei lejake pelunga tere pure khandan ki aurton ko aur usi mei tere saare 🤣🤣🤣🤣🤣🤣khandan ko dafan kr dunga 0 wat ke bulb jitna bana ch00chi hai teri behn ka sala dabane jao toh hath mei hi ni ata bollywood mei asli talent jaisa ch00cha hai🤣🤣🤣🤣🤣🤣 teri ammy ka usko jitna dabao badhta jata hai Teri ammy 🤣🤣🤣🤣🤣🤣ko wheel wali kursi pe baitha ke ch0dunga kacha kach landbhature ki aulaad sale teri ammy ke b00r ka baal se tera gala daba ke maar dalunga tiktok ke chuchidhari betich0d nipple nikal ke teri ammy ka peechwade pe laga dunga tatti khor hai tu sale apni tatti chatne wala suar hai tu  chachundar sale badbudaar prani behnch0d g@nd mei teri belan dal ke faad dunga usme se khun hi khun niklega lawde  insta pe live ch0dunga tere 😍😍😍nani ko patak patak ke HAHAHAHAHA MAADDARCHODDDDDD RANDII KE PILLLE`",
"`TERIIIIIIII MAAAAAAAAAA KI CHUTTTTT MEEEEEEEEE GHODEEEE KA LUNDDDDDDD MADARCHODDDDDDD GASTI KE BAXHEEEEE`",
"MATARCHODDDD RANDI KE PILLEEEE ABHI TERI MAAAAAAA KO AISA CHODUNGA KI GHAR TAK BACCHE HAGTE HUE JAYEGIIIIII",
"TERI MA KAAAAAAAAAA BOXDAAAA AFD DALAAAAAAAAA AAAAAAGG LGAAAAAAAAAAA KRRRRRRRR MADARCHODDDDDDDDDDDDDDDDDD TERAAAAAAAA KHANDAAAANNNNNNNNNNN CJHODDDDDDDDDDD DALAAAAAAAAAAAAAAA",

    ]

@borg.on(admin_cmd(pattern="baap"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RUNSREACTS) - 1)    
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)