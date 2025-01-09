from database.mongodb import DatabaseHelper

def drop_col():
    try:
        collection_list = (
            DatabaseHelper
            .initialize_database()
            .list_collection_names("mongodb://localhost:17017")
        )
        print("Existing collections:")
        for collection in collection_list:
            print(collection)
        collection_drop = input("\nEnter the collection to drop: ")
        if collection_drop in collection_list:
            return (
                DatabaseHelper
                .initialize_database()
                .drop_collection(collection_drop)
            )
    except Exception as e:
        print(f"An error has occurred in db_script: {e}")
    

if __name__ == "__main__":
    pass