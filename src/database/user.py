from pymongo.collection import Collection
from mongodb import DatabaseHelper

class UserCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["doctors"]

    def get_collection() -> Collection:
        return UserCollection.__COLLECTION