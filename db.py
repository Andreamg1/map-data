# db.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Connect to cluster with URI
client = MongoClient(os.environ.get('URI'))
db = client[os.environ.get('DB')]
