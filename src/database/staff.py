from pymongo.collection import Collection
from mongodb import DatabaseHelper

class StaffCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["staff"]

    def get_collection() -> Collection:
        return StaffCollection.__COLLECTION