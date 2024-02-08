# ©️biisal jai shree krishna 😎
from os import environ

API_ID = environ.get('API_ID','')
API_HASH = environ.get('API_HASH','')
BOT_TOKEN = environ.get('BOT_TOKEN','')
BOT_NAME = environ.get('BOT_NAME','BISAL CHAT BOT')
ADMIN = int(environ.get('ADMIN',''))
CHAT_GROUP = int(environ.get('CHAT_GROUP','-1001812797837'))
ADMIN_NAME = environ.get('ADMIN_NAME','Bisal')
LOG_CHANNEL = environ.get('LOG_CHANNEL','')
MONGO_URL = environ.get('MONGO_URL','')
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20 #keep this atleast 20
ONLY_SCAN_IN_GRP = True # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.