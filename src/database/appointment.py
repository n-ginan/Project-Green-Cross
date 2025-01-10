from pymongo.collection import Collection
from mongodb import DatabaseHelper

class AppointmentsCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["appointments"]

    def get_collection() -> Collection:
        return AppointmentsCollection.__COLLECTION