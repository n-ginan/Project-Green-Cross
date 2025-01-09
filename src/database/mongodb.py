from pymongo import MongoClient
from pymongo.database import Database

class DatabaseHelper:

    __client = None
    __database = None
    __preventor = True

    def __new__(cls):
        if cls.__client is None:
            cls.__client = super(DatabaseHelper, cls).__new__(cls)
        return cls.__client
    
    def __init__(self):
        try:
            if DatabaseHelper.__preventor or DatabaseHelper.__database is not None:
                raise Exception("This class implements a singleton pattern, call the initialize_database method instead.")
            DatabaseHelper.__client = MongoClient("mongodb://localhost:27017/")
            DatabaseHelper.__database = DatabaseHelper.__client["ehr"]
            print("Database connection has succeeded")
        except Exception as e:
            print(f"An error in the DatabaseHelper class: {e}")

    @staticmethod
    def initialize_database() -> Database:
        if DatabaseHelper.__database is None and DatabaseHelper.__preventor:
            DatabaseHelper.__preventor = False
            DatabaseHelper()
        return DatabaseHelper.__database
    
if __name__ == "__main__":
    DatabaseHelper.initialize_database()