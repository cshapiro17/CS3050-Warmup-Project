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

        # The keyword will always be the first value in the parsed query
        keyword = parsed_query[0]

        # Determine if the keyword matches a query command
        if (not self.verify_keyword(keyword)):
            return "Command not found."

        if len(parsed_query) == 1:
            
            if keyword == "Help":
                message = "this is a help message"

                return message

        # Handle queries of any length
        elif (len(parsed_query) - 3) % 4 == 0:

            # Create initial element indicies
            keyword_index = 0
            filter_by_index = 1
            attribute_index = 2

            # Create a list to hold the get data expression components
            get_list = []

            # Add first component to the list
            get_list.append(f'self.db.collection("{COLLECTION}")')

            # For each instance of query add a filter component (i.e 'Sport == Football' is one instance)
            for i in range(int(((len(parsed_query) - 3) / 4) + 1)):

                # Verify that the operator is valid
                if (not self.verify_filter(parsed_query[filter_by_index + (4 * i)])):
                    return "Unknown operator."

                # Add component to the list
                get_list.append(
                    f'.where("{parsed_query[keyword_index + (4 * i)]}", "{parsed_query[filter_by_index + (4 * i)]}", "{parsed_query[attribute_index + (4 * i)]}")')

            # Add final component to the list
            get_list.append('.stream()')

            # Join the list into a string
            get = ''.join(get_list)

            # Evaluate the expression
            docs = eval(get)

        else:
            return "Wrong input. Try again"

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

        # Handle no matching data
        if len(list) == 0:
            message = "None"

            return message

        # Print items back to the user
        for i in range(len(list) - 1):
            # Join items into a string
            output_string = output_string + str(list[i]) + ", "

        # Join the final item to the list
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
        

        
            



