from dotenv import load_dotenv
import os

load_dotenv()

def get_token():
    TOKEN = os.getenv("TOKEN")
    return TOKEN

def get_url():
    url = os.getenv("URL")
    return url