import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()

def get_channel_id():
    return int(os.getenv("FORM_SUBMISSION_CHANNEL_ID"))
