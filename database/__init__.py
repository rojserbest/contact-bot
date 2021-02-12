from pymongo import MongoClient

from config import DB_URI

client = MongoClient()
db = client["infowritebot"]
