import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_USERNAME = getenv("BOT_USERNAME")
BOT_NAME = getenv("BOT_NAME")
START_IMAGE = getenv("START_IMAGE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "DURATION_LIMIT"))
STRING_SESSION = getenv("STRING_SESSION")
OWNER_USERNAME = getenv("OWNER_USERNAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "SUDO_USERS").split()))
aiohttpsession = aiohttp.ClientSession()
