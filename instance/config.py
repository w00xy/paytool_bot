import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Loading from .env file
TOKEN = os.getenv('TOKEN')
DB_LITE = os.getenv('DB_LITE')
ADMINS = os.getenv('ADMINS')
