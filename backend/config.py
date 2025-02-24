import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
    UPLOAD_FOLDER = "nfs"
    USER_SECRET_KEY = os.getenv('USER_SECRET_KEY', 'your_user_secret_key_here')

