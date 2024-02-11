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
        # #define parsers for words and characters
        # word_parser = Word(alphas)
        # char_parser = Word(printables, excludeChars=" ")
        # #double quote parser 
        

        # #define a parser for one or more words or characters
        # sentence_parser = ZeroOrMore(word_parser | char_parser )
        # #parse the query
        # parsed_query = sentence_parser.parseString(query_string)

        # return parsed_query
        word_parser = Word(alphas)
        char_parser = Word(printables, excludeChars='" ')

        # Define a parser for quoted strings
        quoted_parser = '"' + Word(printables, excludeChars='"') + '"'

        # Define a parser for one or more words, characters, or quoted strings
        sentence_parser = word_parser | char_parser

        # Parse the query
        parsed_query = []

        # Flag to indicate if the parser is currently within a quoted string
        in_quoted_string = False

        # Temporary buffer to accumulate characters in a quoted string
        quoted_buffer = ""

        # Iterate through the query string
        for char in query_string:
            if char == '"':
                if in_quoted_string:
                    # End of quoted string, add to parsed_query
                    parsed_query.append(quoted_buffer)
                    quoted_buffer = ""
                    in_quoted_string = False
                else:
                    # Start of quoted string
                    in_quoted_string = True
            elif in_quoted_string:
                # Inside a quoted string, use quoted parser
                parsed_query.append(quoted_parser.parseString(query_string).asList()[0])
            else:
                # Outside quoted string, use regular parsers
                parsed_query.append(sentence_parser.parseString(char).asList()[0])

        # If there's anything left in the quoted_buffer, add it to parsed_query
        if quoted_buffer:
            parsed_query.append(quoted_buffer)

        # Join the parsed tokens into a single string
        parsed_query = ' '.join(parsed_query)

        print(parsed_query)

        return parsed_query
    
    def double_quote(self, query_string):
        # check double quote is in
        # double_quote_string = ""
        # if (query_string.contains('"')):
        #     for char in query_string:
        #         if (char == '"'):
        #             double_quote_string += char
        
        pass 



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

    
