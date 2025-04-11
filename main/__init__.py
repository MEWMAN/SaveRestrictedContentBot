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
SESSION = config("1BJWap1sBu6a-pbD0Kr-49KoVZAV-04CVgTCv3YNwfhxqHHBVp1dP5ENuJmHcnnNXc0wHitgU4JcSmCasCUFpt32HOzwpfdB9D7SfYFaTbgjcszWoIYiGt0eAypTC7oJqDzxiV--b9vdkawzdQBC7kyXw89VMfICi4h5Uh5kSopkH55kNlyU_II_VDlwisQYYcHyguvXluiq1E5yNsuHUY3ilKq1i0TAAWP6RHkHdckg0Q5gr-o_Y2e6qvPVobcbO4iqIG3VOnrSJPJQS8xz8bGXjXz51LYJFExzxoqvl84ARewuhgKAZBBdY5aOhL5sLbX4JciDyvASnIxzZBTwqApaRNtAXX98=", default=None)
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
