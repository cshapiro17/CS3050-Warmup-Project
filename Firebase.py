import firebase_admin # if gettting error run in cmd: pip3 install firebase_admin
from firebase_admin import firestore, credentials

COLLECTION = 'SmithAthletes'

class Firebase:

    def __init__(self) -> None:
        # Add credentials to make connection
        cred = credentials.Certificate("smithathletes-d8741-firebase-adminsdk-snc4k-3e47fd0006.json")
        firebase_admin.initialize_app(cred, {"databaseURL": "https://smithathletes-d8741-default-rtdb.firebaseio.com/"})

        # Works on SmithAthlete collection, can change later if collections are added
        self.db = firestore.client()
        self.collection_ref = self.db.collection(COLLECTION)

    def connect(self):
        pass
        
    def retrieve_all_data(self):
         return self.collection_ref.get()

    def process_query(self, parsed_query):

        keyword = parsed_query[0]

        if (not self.verify_keyword(keyword)):
            return "Column name not found."

        if len(parsed_query) == 1:
            if keyword == "help":
                message = "This is a help message"

                return message

        if len(parsed_query) == 3:
            filter_by = parsed_query[1]
            attribute = parsed_query[2]

            if (not self.verify_filter(filter_by)):
                return "Unknown operator."
        
            docs = (
                self.db.collection(COLLECTION)
                .where(keyword, filter_by, attribute)
                .stream()
            )

            # Create a list to hold values
            list = []

            # Create string to return to user
            output_string = ""

            for doc in docs:

                # Get the filtered items in a dictionary
                results = doc.to_dict()

                # Only take the first name and append "Smith"
                list_item = results["First Name"] + " Smith"

                # Append to the list
                list.append(list_item)

            if len(list) == 0:
                message = "None"

                return message

            # Print items back to the user
            for i in range(len(list) - 1):
                output_string = output_string + str(list[i]) + ", "

            output_string = output_string + list[len(list) - 1]

            return output_string

    def get_query_from_user(self):
        user_input = input("->  ")

        return user_input
    
    def get_column_titles(self):
        # Pull data from firebase
        docs = self.retrieve_all_data()

        column_dict = dict()
        for item in docs:
            column_dict = item.to_dict()
            break

        columns = []
        for key, _ in column_dict.items():
            columns.append(key)
        
        return columns
    
    def verify_keyword(self, keyword):
        columns = self.get_column_titles()
        
        if (keyword in columns):
            return True
        
        return False    
        
    def verify_filter(self, filter_by):
        valid_filter = ["<", "<=", "==", '>', '>=', '!=', 'array-contains', 'array-contains-any', 'in', 'not-in']

        if (filter_by in valid_filter):
            return True
        return False
        

        
            



