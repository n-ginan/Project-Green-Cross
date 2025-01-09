from pymongo.collection import Collection
from bson import ObjectId
from mongodb import DatabaseHelper

class UserCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["doctors"]

    def get_collection() -> Collection:
        return UserCollection.__COLLECTION
    
    # CREATE
    def insert_user(username: str, password: str, role: str):
        """Returns None if user exists, and returns the inserted_id if successful"""
        try:
            if UserCollection.has_user(username):
                return None
            return (
                UserCollection
                .get_collection()
                .insert_one(
                    {
                        "username": username,
                        "password": password,
                        "role": role
                    }
                )
                .inserted_id
            )
        except Exception as e:
            print(f"An error has occurred at UserCollection: {e}")

    # READ
    def has_user(username: str):
        """Checks if user exists"""
        try:
            return (
                UserCollection
                .get_collection()
                .find_one(
                    {
                        "username": username
                    }
                )
            )
        except Exception as e:
            print(f"An error has occurred at UserCollection: {e}")

    def get_user_by_id(user_id: str):
        """Gets the user by the id, mostly used for authentication purposes"""
        try:
            return (
                UserCollection
                .get_collection()
                .find_one(
                    {
                        "_id": ObjectId(user_id)
                    }
                )
            )
        except Exception as e:
            print(f"An error has occurred at UserCollection: {e}")
    
    # UPDATE
    # DELETE
