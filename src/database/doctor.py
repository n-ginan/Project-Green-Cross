from pymongo.collection import Collection
from mongodb import DatabaseHelper
from user import UserCollection

class DoctorCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["doctors"]

    def get_collection() -> Collection:
        return DoctorCollection.__COLLECTION
    
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
            if DoctorCollection.has_doctor(doctor_name):
                return None
            return (
                DoctorCollection
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
            print(f"An error has occurred at DoctorCollection: {e}")

    # READ
    def has_doctor(doctor_name: dict[str, str]):
        """Check if the doctor exists in the database"""
        try:
            return (
                DoctorCollection
                .get_collection()
                .find(
                    {"doctor_name": doctor_name}
                )
            )
        except Exception as e:
            print(f"An error has occurred at DoctorCollection: {e}")