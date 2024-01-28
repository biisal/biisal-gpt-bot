# ©️biisal jai shree krishna 😎
import pymongo
from info import *
client = pymongo.MongoClient(MONGO_URL)
db = client["biisal-ai"]
userList = db.userList


def addUser(userId , userName):
    dets = {
        'userId': userId,
        'userName': userName
    }
    userList.insert_one(dets).inserted_id
    return