import asyncio
import base64
import os
import random
import shutil
import time
from datetime import datetime
from telethon.errors import FloodWaitError
from telethon.tl import functions
from config import BIO

DEL_TIME_OUT = 60
normzltext = "1234567890"
namerzfont = "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"

LOGS = logging.getLogger(__name__)

@jmthon.on(events.NewMessage(outgoing=True, pattern=".اسم وقتي"))
async def _(event):
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{HM}"
        LOGS.info(name)
        try:
            await jmthon(
                functions.account.UpdateProfileRequest(
                    first_name=name
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)

@jmthon.on(events.NewMessage(outgoing=True, pattern=".بايو وقتي"))
async def _(event):
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%H:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        bio = f"{DEFAULTUSERBIO} |️ {HM}"
        LOGS.info(bio)
        try:
            await jmthon(
                functions.account.UpdateProfileRequest(
                    about=bio
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)