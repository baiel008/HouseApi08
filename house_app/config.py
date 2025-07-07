import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_LIFETIME = 30
REFRESH_TOKEN_LIFETIME = 3


class Settings:
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_SECRET = os.getenv('GOOGLE_SECRET')
    GOOGLE_URL = os.getenv('GOOGLE_URL')
settings = Settings