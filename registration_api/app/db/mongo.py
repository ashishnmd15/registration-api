from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING

client = AsyncIOMotorClient("mongodb+srv://ashfa1510:BDdlXuF0kgMSLPp4@resume.qv7o7rf.mongodb.net/")
db = client["registration"]
users_collection = db["user"]
blacklist_collection = db["list-collection"]

blacklist_collection.create_index(
    [("expires_at", ASCENDING)],
    expireAfterSeconds=0  
)