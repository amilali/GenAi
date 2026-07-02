# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.
# _ = ...: In Python, the underscore _ is a convention used for a throwaway variable.
# load_dotenv() returns True if it successfully found and loaded a .env file, or False if it didn't.
# Since we only care about the action of loading the variables and don't need to do anything with the return value itself,
# we assign it to _ to discard it.                                                                                                                  # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())

def get_openrouter_api_key():
    load_env()
    openrouter_api_key = os.getenv('OPENROUTER_API_KEY')
    os.environ["OPENROUTER_API_KEY"] = openrouter_api_key
    os.environ["OPENROUTER_API_BASE"] = "https://openrouter.ai/api/v1"
    os.environ["OPENROUTER_MODEL_NAME"] = 'mistralai/mistral-7b-instruct'
    return openrouter_api_key



