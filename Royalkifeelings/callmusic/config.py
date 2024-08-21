from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME: str = getenv("SESSION_NAME", "BAE6FqgAdJ949BdJ2XgV84zEGv83HUG4Ij9PVd5bZibvJpCfR9u6WSvZqOW-sjUYdG5i-vfJP1KtBkRq6U5DBycNd9NiyW5f5vY6VeBmeRGkMwilnu1aXEaUx4O5wEQ5zFvK897lwh0DhhPRWDDph3xsxW9IV-0NMalxhcqSoXLyht3KeQphvCMyfMY4vqi6tEwqCxC2xva3QUbQ_6vGiMeqQQlStT4J0af0vPlOgSxwPU9e3Z4w-ettozsL-hFIPqlIWsWO7S-3116Cz62gY9Jq2nZH1pPVDZZDkRmyb6NVjGdMmSm0rDVcEOEqv9WR-G-gQ_GMr66uagWu9jG1wZU8U6_uzAAAAAG4lsWeAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
BOT_USERNAME = getenv("BOT_USERNAME", "mehmetbeyasistanibot")
BOT_TOKEN = getenv("BOT_TOKEN", "7387514914:AAFCbnny8x8zYlG1DYNAazL2VRJyrN95jEI")
API_ID = int(getenv("API_ID", "20584104"))
API_HASH = getenv("API_HASH", "f325ee578444d70ad2d02b0673f94d3a")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/kumsalmuzikk")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/kumsaldestekkanal")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7391856030").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7391856030").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "12000"))
PMPERMIT = getenv("PMPERMIT", "ENABLE")
BOT_NAME = getenv("BOT_NAME","kumsalmusic")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/musickss-03-12")
