import os
from dotenv import load_dotenv


load_dotenv()


user_name = os.environ.get['USER_NAME']
password = os.environ["PASSWORD"]