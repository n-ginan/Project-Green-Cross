from pymongo.collection import Collection
from pymongo.cursor import Cursor
from mongodb import DatabaseHelper
from bson import ObjectId

class PatientsCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["patients"]

    def get_collection() -> Collection:
        try:
            return PatientsCollection.__COLLECTION
        except Exception as e:
            print(f"An error occurred at the PatientsCollection: {e}")
    
    # CREATE
    def insert_patient(
      patient_name: dict[str, str],
      demograph: dict[str, str | int],
      contact: dict[str, str],
      address: dict[str, str],
      insurance: dict[str, str] | None,
      emergency_contacts: list[dict[str, str]] | None,
      allergies: list[str] | None,
      active_medications: list[str] | None,
      medical_balance: float,
      admission: list[dict[str, str]] | None
    ):
        """
        Will return None if patient already exists in the database,
        if not it will return an ObjectId
        """
        try:
            collection = PatientsCollection.get_collection()
            patient_fullname = {
                "first_name": patient_name["first_name"],
                "middle_initial": patient_name["middle_initial"],
                "last_name": patient_name["last_name"],
                "suffix": patient_name["suffix"]
            }
            demograph_data = {
                "age": demograph["age"],
                "birth": demograph["birth"],
                "gender": demograph["gender"],
                "sex": demograph["sex"],
                "ethnicity": demograph["ethnicity"],
            }
            if PatientsCollection.has_patient(patient_fullname, demograph):
                return None
            patient_data = {
                "patient_name": patient_name,
                "demograph": demograph,
                "contact": contact,
                "address": address,
                "insurance": insurance,
                "emergency_contacts": emergency_contacts,
                "allergies": allergies,
                "active_medications": active_medications,
                "medical_balance": medical_balance,
                "admission": admission
            }
            return collection.insert_one(patient_data).inserted_id
        except Exception as e:
            print(f"An error occurred at the PatientsCollection: {e}")

    # READ
    def has_patient(patient_name: dict[str, str], demograph: dict[str, str | int]) -> Cursor:
        """Checks if patient document exists in the database"""
        try:
            collection = PatientsCollection.get_collection()
            data = {
                "patient_name": {
                    "first_name": patient_name["first_name"],
                    "middle_initial": patient_name["middle_initial"],
                    "last_name": patient_name["last_name"],
                    "suffix": patient_name["suffix"]
                },
                "demograph": {
                    "age": demograph["age"],
                    "birth": demograph["birth"],
                    "gender": demograph["gender"],
                    "sex": demograph["sex"],
                    "ethnicity": demograph["ethnicity"],
                }
            }
            return collection.find(data)
        except Exception as e:
            print(f"An error occurred at the PatientsCollection: {e}")

    def get_patient_id(patient_name: dict[str, str], demograph: dict[str, str | int]) -> str:
        """Returns the string representation of the patient _id ObjectId"""
        try:
            collection = PatientsCollection.get_collection()
            data = {
                "patient_name": patient_name,
                "demograph": demograph
            }
            return str(collection.find_one(data, {"_id": 1})["_id"])
        except Exception as e:
            print(f"An error occurred at the PatientsCollection: {e}")
        