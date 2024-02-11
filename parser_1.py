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
        # define parsers for words and characters
        double_quote_string = ""
        if ('"' in query_string):
            double_quote_string = self.double_quote(query_string)

        word_parser = Word(alphas)
        char_parser = Word(printables, excludeChars=" ")
        #double quote parser 

        #define a parser for one or more words or characters
        sentence_parser = ZeroOrMore(word_parser | char_parser )
        #parse the query
        parsed_query = sentence_parser.parseString(query_string)

        if (double_quote_string != ""):
            temp = []
            temp.append(parsed_query[0])
            temp.append(parsed_query[1])
            temp.append(double_quote_string)
            parsed_query = temp

        return parsed_query
    
    def double_quote(self, query_string):
        # check double quote is in
        double_quote_string = ""
        quote_count = 0
        for char in query_string:
            if (char == '"'):
                quote_count += 1
            elif (quote_count == 1):
                double_quote_string += char

        return double_quote_string



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

    
