import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

# Attempt to connect to the database
try:
    client = MongoClient(os.getenv("URI"))
    db = client["bit-billionaire"]
    collection = db["test-environment"]
except Exception as e:
    print(f"Error connecting to the database: {e}")
