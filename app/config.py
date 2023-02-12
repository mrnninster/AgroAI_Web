import os
from dotenv import load_dotenv

load_dotenv('app/.env')
app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    is_production = os.environ.get("IS_PRODUCTION")
    if is_production == 'True':
        ENV = "production"
    else:
        ENV = "development"