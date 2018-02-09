import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
GIST_TOKEN = os.environ.get("GIST_TOKEN")
GIST_API_URL = os.environ.get("GIST_API_URL")
GIST_PUBLIC_URL = os.environ.get("GIST_PUBLIC_URL")
PHONE_NUMBER_TO = os.environ.get("PHONE_NUMBER_TO")
PHONE_NUMBER_FROM = os.environ.get("PHONE_NUMBER_FROM")