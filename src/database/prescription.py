from pymongo.collection import Collection
from mongodb import DatabaseHelper

class PrescriptionCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["prescriptions"]

    def get_collection() -> Collection:
        return PrescriptionCollection.__COLLECTION