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
        
    def retrieveAllData(self):
        # document_data = collection_ref.document('your_document_id').get().to_dict()
        print(self.collection_ref.get())

    def processQuery(self):

        # Test with 'Sport == Football'
        docs = (
            self.db.collection("SmithAthletes")
            .where("Sport", "==", "Football")
            .stream()
        )

        for doc in docs:
            print(f"{doc.id} => {doc.to_dict()}")



