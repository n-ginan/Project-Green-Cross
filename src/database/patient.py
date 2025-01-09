from pymongo.collection import Collection
from mongodb import DatabaseHelper
from bson import ObjectId

class PatientCollection:

    __COLLECTION = DatabaseHelper.initialize_database()["patients"]

    def get_collection() -> Collection:
        try:
            return PatientCollection.__COLLECTION
        except Exception as e:
            print(f"An error occurred at the PatientsCollection: {e}")
    
    def has_patient(patient_name: dict):
        """Checks if patient document exists in the database"""
        try:
            collection = PatientCollection.get_collection()
            patient_fullname = {
                "name.first_name": patient_name["first_name"],
                "name.middle_initial": patient_name["middle_initial"],
                "name.last_name": patient_name["last_name"],
                "name.suffix": patient_name["suffix"]
            }
            return collection.find(patient_fullname)
        except Exception as e:
            print(f"An error occurred at the PatientsCollection: {e}")

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
            collection = PatientCollection.get_collection()
            patient_fullname = {
                    "first_name": patient_name["first_name"],
                    "middle_initial": patient_name["middle_initial"],
                    "last_name": patient_name["last_name"],
                    "suffix": patient_name["suffix"]
            }
            if PatientCollection.has_patient(patient_fullname):
                return None
            patient_data = {
                "name": patient_name,
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
        