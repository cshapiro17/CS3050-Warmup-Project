
class Parser:
    def __init__(self):
        print("init")

    def parseQuery(self, queryString): 
        '''
        Takes a query string as input
        and parses it into a format that 
        the datastore component can understand.
        Returns string that is in valid format to get information from the firebase
        '''
        print('parseQuery')

    def executeQuery(self, parsedQuery): 
        '''
        Sends the parsed query to the
        datastore for execution 
        Returns the data retrieve from the firebase 
        '''
        print('execute')

    def getData(self, queryResults): 
        '''
        May not need this method
        Takes the information from the firebase and 
        returns the specefic information requested from
        the query
        '''
        print('getData')
