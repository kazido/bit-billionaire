import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

URI = os.getenv('URI')

try:
    client = MongoClient(URI)
    db = client["bit-billionaire"]
    collection = db["test-environment"]
except Exception as e:
    print(f"Error connecting to the database: {e}")
