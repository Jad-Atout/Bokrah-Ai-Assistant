import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv("BASE_URL")
AUTH_HEADER = {"Authorization": f"JadRazanHuda__{os.getenv('API_TOKEN')}"}
CLIENT_ID = os.getenv("CLIENT_ID")
DATABASE_URI = os.getenv("DATABASE_URI")
