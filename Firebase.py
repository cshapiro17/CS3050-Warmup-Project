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

    def process_query(self, parsed_query):

        # The keyword will always be the first value in the parsed query
        keyword = parsed_query[0]

        if (len(parsed_query) == 1 and (keyword == "help" or keyword == "*")):
            if keyword == "help":
                # Open help file and print its contents 
                with open('help.txt', 'r') as file:
                    file_content = file.read()
                    print(file_content)
                return "\n:)"
            elif keyword == "*":
                self.print_all_data(self.retrieve_all_data())
                return "\nAll items in data base disaplyed."

        elif (not self.verify_keyword(keyword)):
            return "Column name not found."
        
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
            list_item = results["first_name"] + " Smith"

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
        """
        Gets the query input from the user
        :return user_input, str
        """
        user_input = input("->  ")

        return user_input
    
    def get_column_titles(self):
        """
        Gets the column titles from the database
        :return columns: list of all column names
        """
        # Pull data from firebase
        column_dict = self.retrieve_all_data()

        # # Get the first item to a dictionary
        # column_dict = dict()
        # for item in docs:
        #     column_dict = item.to_dict()
        #     break

        # # loop through dictionary and add all the keys to columns list 
        columns = []
        for key, _ in column_dict[0].items():
            columns.append(key)
        
        return columns
    
    def verify_keyword(self, keyword):
        """
        Checks the keyword given is a valid colum name
        :param keyword: column name given by user
        :type keyword: str
        :return boolean
        """
        columns = self.get_column_titles()
        
        if (keyword in columns):
            return True
        
        return False    
        
    def verify_filter(self, filter_by):
        """
        Checks the filter given is a valid operator
        :param filter_by: operator given by user
        :type keyword: str
        :return boolean
        """
        valid_filter = ["<", "<=", "==", '>', '>=', '!=', 'array-contains', 'array-contains-any', 'in', 'not-in']

        if (filter_by in valid_filter):
            return True
        return False
    
    def retrieve_all_data(self):
        """
        Retrieves everything from database, converts each item to a dictionary and adds it to a list
        :return list_of_dict: list where each item in list is dictionary 
        """
        docs = self.collection_ref.get()
        list_of_dict = []
        for item in docs:
            list_of_dict.append(item.to_dict())
        return list_of_dict
    
    def print_all_data(self, list_of_dict):
        """
        Prints all the data in the following format:
        Team: Dallas Cowboys
        first_name: Tyron
        id: 6
        Birthdate: December 12, 1990
        Sport: Football
        Death Date: 
        Championship: 0

        :param list_of_dict: list of dictionaries of 
        """
        for item in list_of_dict:
            print("")
            for key, value in item.items():
                print(str(key) + ": " + str(value))
        

        
            



