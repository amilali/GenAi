# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.                                                                                                                     # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())

def get_openrouter_api_key():
    load_env()
    openrouter_api_key = os.getenv('OPENROUTER_API_KEY')
    os.environ["OPENROUTER_API_KEY"] = openrouter_api_key
    os.environ["OPENROUTER_API_BASE"] = "https://openrouter.ai/api/v1"
    os.environ["OPENROUTER_MODEL_NAME"] = 'mistralai/mistral-7b-instruct'
    return openrouter_api_key



