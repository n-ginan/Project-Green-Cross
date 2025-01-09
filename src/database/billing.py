from pymongo.collection import Collection
from mongodb import DatabaseHelper

class BillingCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["billings"]

    def get_collection() -> Collection:
        return BillingCollection.__COLLECTION