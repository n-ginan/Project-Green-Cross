from pymongo.collection import Collection
from mongodb import DatabaseHelper

class AppointmentCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["appointments"]

    def get_collection() -> Collection:
        return AppointmentCollection.__COLLECTION