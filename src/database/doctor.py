from pymongo.collection import Collection
from mongodb import DatabaseHelper

class DoctorCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["doctors"]

    def get_collection() -> Collection:
        return DoctorCollection.__COLLECTION