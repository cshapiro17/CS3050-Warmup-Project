import firebase_admin # if gettting error run in cmd: pip3 install firebase_admin
from firebase_admin import firestore, credentials

class Firebase1:

    def __init__(self) -> None:
        # Add credentials to make connection
        cred = credentials.Certificate("smithathletes-d8741-firebase-adminsdk-snc4k-3e47fd0006.json")
        firebase_admin.initialize_app(cred, {"databaseURL": "https://smithathletes-d8741-default-rtdb.firebaseio.com/"})

        # Works on SmithAthlete collection, can change later if collections are added
        self.db = firestore.client()
        self.collection_ref = self.db.collection('SmithAthletes')

    def connect(self):
        pass
        
    def retrieve_all_data(self):
        # document_data = collection_ref.document('your_document_id').get().to_dict()
        print(self.collection_ref.get())

    def process_query(self,keyword, filter_by, attribute):

        # Test with 'Sport == Football'
        docs = (
            self.db.collection("SmithAthletes")
            .where(keyword, filter_by, attribute)
            .stream()
        )

        # Create a list to hold values
        list = []

        for doc in docs:

            # Get the filtered items in a dictionary
            item = doc.to_dict()

            # Only take the first name and append "Smith"
            list_item = item["First Name"] + " Smith"

            # Append to the list
            list.append(list_item)

        print(list)
            



