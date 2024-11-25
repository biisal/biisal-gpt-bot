# ©️biisal jai shree krishna 😎
from info import *
from motor import motor_asyncio
client = motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client["biisal"]


class User:
    def __init__(self):
        self.users = db["users"]
        self.cache = {}

    async def addUser(self, user_id: int, name: str) -> dict | None:
        try:
            user = {"user_id": user_id, "name": name}
            await self.users.insert_one(user)
            self.cache[user_id] = user      
            return user
        except Exception as e:
            print("Error in addUser: ", e)
            

    async def get_user(self, user_id: int) -> dict | None:
        try:
            if user_id in self.cache:
                return self.cache[user_id]
            user = await self.users.find_one({"user_id": user_id})
            return user
        except Exception as e:
            print("Error in getUser: ", e)
            return None

    async def remove_user(self, user_id: int) -> bool:
        try:
            await self.users.delete_one({"user_id": user_id})
            del self.cache[user_id]
            return True
        except Exception as e:
            print("Error in removeUser: ", e)
            return False
    async def get_or_add_user(self, user_id: int, name: str) -> dict | None:
        user = await self.get_user(user_id)
        if user is None :
            user = await self.addUser(user_id, name)
        return user
    
    async def get_all_users(self) -> list:
        try:
            users = []
            async for user in self.users.find():
                users.append(user)
            return users
        except Exception as e:
            print("Error in getAllUsers: ", e)
            return []


class ChatHistory:
    def __init__(self):
        self.history = db["history"]

    async def add_history(self, user_id: int, history: list) -> bool:
        try:
            recent_history = history[-50:] # increesing this will create a api error
            query = {"user_id": user_id}
            update = {"$set": {"history": recent_history}}
            await self.history.update_one(query, update, upsert=True)
            return True
        except Exception as e:
            print("Error in addHistory: ", e)
            return False


    async def get_history(self, user_id: int) -> list:
        try:
            history = await self.history.find_one({"user_id": user_id})
            return history["history"] if history else []
        except Exception as e:
            print("Error in getHistory: ", e)
            return []
    
    async def reset_history(self, user_id: int) -> bool:
        try:
            await self.history.delete_one({"user_id": user_id})
            return True
        except Exception as e:
            print("Error in clearHistory: ", e)
            return False


chat_history = ChatHistory()
users = User()
