from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "15481135"))
API_HASH = environ.get("API_HASH", "2f1bc8786f6f8d6902bafd8896d6aa80")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "7273878841")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1002362771861")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://mongodb7575:mkCNT8b2LZJX5ekf@cluster0.bcuh8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
