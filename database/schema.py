from database import collection
from pydantic import BaseModel

class UserSchema(BaseModel):
    # Base
    username: str
    password: str
    logged_in: bool = False
    is_new: bool = True
    
    # Economy
    bits: int = 0
    luckbucks: int = 0
    level: int = 0
    
    # Skills
    # Foraging
    forgaging: dict = {
        "level": 1,
        "xp": 0,
    }
    farming: dict = {
        "level": 1,
        "xp": 0,
    }
    fishing: dict = {
        "level": 1,
        "xp": 0,
    }
    farming: dict = {
        "level": 1,
        "xp": 0,
    }
    combat: dict = {
        "level": 1,
        "xp": 0,
    }

# Validate and fill missing fields
def validate_document(username):
    document = collection.find_one({"username": username})
    if not document:
        # Create a new document if it doesn't exist
        user = UserSchema(username=username)
        collection.insert_one(user.model_dump())
    else:
        # Validate and update missing fields
        user = UserSchema(**document)
        collection.update_one({"_id": document["_id"]}, {"$set": user.model_dump()})
