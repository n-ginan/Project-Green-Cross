from pymongo.collection import Collection
from mongodb import DatabaseHelper

class BillingsCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["billings"]

    def get_collection() -> Collection:
        return BillingsCollection.__COLLECTION