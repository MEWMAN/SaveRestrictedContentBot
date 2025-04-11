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
SESSION = config("BAAAAAAApr6lsPQqv7j0qhVkBX7TgJWBMK_dg3B-HGoccFWnV0_kQ24mYdyec1dzTAeK2BTglxKYJqwJQWm3fYc7PCl90H0PtJ9gVpNuCNyzNaghiIa3R4DKlMLugmoPPGJX75v292RrDN1AELuTJfDz1Ux8gKLiHlSHmRKimQfnmQ2XJT8gj9UOXCKxBhhwfKC69eW6KrUTnI2y4dRjeKUqrWLRMABY_pEeQd1ySDRDmCv6j9jZ7qq89Whtxs7iKogbdU6etIk8lBLzHPxsZeNfPnUtgkUTHPGiq-XzgBF7C6GAoBkEF1jlo6EvmwttfglyIPK8BKcjHNkFPCoClpE20Bdf3wAAAAAAACcPAA", default=None)
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
