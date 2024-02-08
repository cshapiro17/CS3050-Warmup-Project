
class Parser:
    def __init__(self):
        print("init")

    def parseQuery(query_string): 
        '''
        Takes a query string as input
        and parses it into a format that 
        the datastore component can understand.
        Returns string that is in valid format to get information from the firebase
        '''
        #define parsers for words and characters
        word_parser = Word(alphas)
        char_parser = Word(printables, excludeChars=" ")

        #define a parser for one or more words or characters
        sentence_parser = ZeroOrMore(word_parser | char_parser)

        #parse the query
        parsed_query = sentence_parser.parseString(query_string)


        return parsed_query

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
