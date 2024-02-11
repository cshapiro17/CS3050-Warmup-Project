from pyparsing import Word, alphas, printables, ZeroOrMore, quotedString

class Parser:
    def __init__(self):
        print("init")

    def parse_query(self, query_string): 
        '''
        Takes a query string as input
        and parses it into a format that 
        the datastore component can understand.
        Returns string that is in valid format to get information from the firebase
        '''
        #define parsers for words and characters
        word_parser = Word(alphas)
        char_parser = Word(printables, excludeChars=" ")
        #double quote parser 
        quoted_parser = quotedString.setParseAction(lambda t: t[0][1:-1])

        #define a parser for one or more words or characters
        sentence_parser = ZeroOrMore(word_parser | char_parser | quoted_parser)
        #parse the query
        parsed_query = sentence_parser.parseString(query_string)

        return parsed_query

    def execute_query(self, parsed_query): 
        '''
        Sends the parsed query to the
        datastore for execution 
        Returns the data retrieve from the firebase 
        '''
        print('execute')

    def get_data(self, query_results): 
        '''
        May not need this method
        Takes the information from the firebase and 
        returns the specefic information requested from
        the query
        '''
        print('getData')
