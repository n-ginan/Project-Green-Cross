from pymongo.collection import Collection
from mongodb import DatabaseHelper
from user import UserCollection

class DoctorsCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["doctors"]

    def get_collection() -> Collection:
        return DoctorsCollection.__COLLECTION
    
    # CREATE
    def insert_doctor(
        doctor_name: dict[str, str],
        specialty: str,
        contact: dict[str, str],
        available_hours: list[dict[str, str | list[str]]],
        department: str,
        room_number: str
    ):
        """
        Returns None if doctor already exists in the database,
        if not the inserted_id will be returned
        """
        try:
            if DoctorsCollection.has_doctor(doctor_name):
                return None
            return (
                DoctorsCollection
                .get_collection()
                .insert_one(
                    {
                        "doctor_name": doctor_name,
                        "specialty": specialty,
                        "contact": contact,
                        "available_hours": available_hours,
                        "department": department,
                        "room_number": room_number
                    }
                )
            ).inserted_id
        except Exception as e:
            print(f"An error has occurred at DoctorsCollection: {e}")

    # READ
    def has_doctor(doctor_name: dict[str, str], specialty: str):
        """Check if the doctor exists in the database"""
        try:
            return (
                DoctorsCollection
                .get_collection()
                .find(
                    {
                        "doctor_name": doctor_name,
                        "specialty": specialty
                    },
                    {
                        "_id": 0,
                        "doctor_name": 1
                    }
                )
            )
        except Exception as e:
            print(f"An error has occurred at DoctorsCollection: {e}")

    def get_doctor_id(doctor_name: dict[str, str], specialty: str):
        """Returns the string representation of the doctor _id ObjectId"""
        try:
            return (
                DoctorsCollection
                .get_collection()
                .find_one(
                    {
                        "doctor_name": doctor_name,
                        "specialty": specialty
                    },
                    {
                        "_id": 1,
                    }
                )
            )
        except Exception as e:
            print(f"An error has occurred at DoctorsCollection: {e}")