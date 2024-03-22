from . import app as application
from dotenv import load_dotenv

import os

load_dotenv(os.getenv("API_ENVFILE"))

if __name__ == '__main__':
    application.run()
