import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = int(os.environ.get("REDIS_PORT"))
REDIS_DB = os.environ.get("REDIS_DB")