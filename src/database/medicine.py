from pymongo.collection import Collection
from mongodb import DatabaseHelper

class MedicinesCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["medicines"]

    def get_collection() -> Collection:
        return MedicinesCollection.__COLLECTION