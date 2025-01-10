from pymongo.collection import Collection
from mongodb import DatabaseHelper

class PrescriptionsCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["prescriptions"]

    def get_collection() -> Collection:
        return PrescriptionsCollection.__COLLECTION
    
    # CREATE
    def insert_prescription():
        pass
    
    # READ
    # UPDATE
    # DELETE