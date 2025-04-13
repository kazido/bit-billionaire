from database import collection
from database.schema import validate_document


class User:
    def __init__(self, username: str):
        self.username = username
        self.query = {"username": username}
        validate_document(username)

    def __str__(self):
        return self.username

    def get_profile(self):
        lines = (
            f"Profile: {self.username}",
            f"{'=' * (len(self.username) + 9)}",
            f"Bits: {self.get_bits()}",
            f"Level: {self.get_field('level')}",
        )
        return lines

    @staticmethod
    def login(username: str, password: str) -> object:
        # Username/password combo not found, return code 1
        if not collection.find_one({"username": username, "password": password}):
            return 1
        user = User(username=username)

        # User was already logged in, return code 2
        if user.get_field("logged_in") == True:
            return 2

        # Successfully logged in!
        user.set_field("logged_in", True)
        return user

    @staticmethod
    def new_user(username: str, password: str) -> bool:
        user = {
            "username": username,
            "password": password,
            "logged_in": False,
            "bits": 0,
            "level": 0,
        }

        return bool(collection.insert_one(user))

    def set_field(self, field: str, value):
        return collection.update_one(self.query, {"$set": {field: value}})

    def get_field(self, field: str):
        # UGLY UGLY UGLY!!!
        return collection.find(self.query, {"_id": 0, field: 1})[0][field]

    def get_bits(self):
        return self.get_field("bits")
