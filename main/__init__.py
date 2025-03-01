#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("21248884", default=None, cast=int)
API_HASH = config("25c51c205e114ff4574b095cdb924752", default=None)
BOT_TOKEN = config("7952935242:AAF-0cqZbfGrFkHh_3Z_BjmkUTL3yl39WYU", default=None)
SESSION = config("BAFEO3QAehM8BGarnU3Jigl2Tkm7nZcph1My1L3PyZig4HeYKktMCGw6XFBwkOcy9prnMcDSPibeaUs6eYfO8eGNTSKv1fBSndJIBiqMEPlnqKW-uNjIENNLze2nmBG-Lv-ub3f0uoI1P0DFmOrNRHm6ITTrwobWjOR8MAdhuN7cPTnCaSBAPCF9ahdMPZ5fKYp9XZIXsvoRG6O04QuIhmBLqv0Ien-aHJ7hKQ1DX2uj7GePTzbVaAg8C_7Yw5UOcJ9g6YGhSix4R7b4DaC6q6ZkgUVEH_wV3Mbe1CVWruS-2LYDqgw5VYPA2jONXUmcs-iQLuL0WfI4KXQYQTCPMIELc_QKkgAAAAHn5G_uAA", default=None)
FORCESUB = config("d4q44", default=None)
AUTH = config("8185475054", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
