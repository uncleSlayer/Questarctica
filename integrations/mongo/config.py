
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.env import settings

uri = f"mongodb+srv://{settings.MONGO_DB_USERNAME}:{settings.MONGO_DB_PASSWORD}@cluster0.lsl8bmh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
mongo_db = client.get_database("questarctica")
github_issues_collection = mongo_db.get_collection("github-issues")