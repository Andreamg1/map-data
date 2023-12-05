from pymongo import MongoClient
from dotenv import load_dotenv
import os


# Load .env as environment variables
load_dotenv()

# Connect to cluster with URI
client = MongoClient(os.environ.get('URI'))
db = client[os.environ.get('DB')]
