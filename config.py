import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22349465"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3732e079c4125690226d8e7b4e028ca4")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://teekam_jaat:9571404334@teekam.rkeoopf.mongodb.net/?retryWrites=true&w=majority&appName=Teekam")
