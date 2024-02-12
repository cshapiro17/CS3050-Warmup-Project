from pyparsing import Word, alphas, printables, ZeroOrMore, quotedString
import re

class Parser:
    def __init__(self):
        print("init")

    def parse_query(self, query_string): 
        '''
        Takes a query string as input
        and parses it into a format that 
        the datastore component can understand.
        Returns string that is in valid format to get information from the firebase

        :param query_string: raw string entered by user
        :return parsed_query: list where each element is characters entered by user, ex ['sport', '==', 'Football']
        '''
        # Declare double_quote_string to to empty
        double_quote_string = ""

        # Check if there is a double quote in the raw query string
        if ('"' in query_string):
            # Extracts the words inside the double quotes
            double_quote_string = self.double_quote(query_string)

        # define parsers for words and characters
        word_parser = Word(alphas)
        char_parser = Word(printables, excludeChars=" ")
        #double quote parser 

        #define a parser for one or more words or characters
        sentence_parser = ZeroOrMore(word_parser | char_parser )
        #parse the query
        parsed_query = sentence_parser.parseString(query_string)

        # If there was a valid quoted string entered, ex "Denver Broncos"
        if (double_quote_string != ""):
            temp = parsed_query
            # Loop through parsed_query until the double quote item is found
            for i in range(0, len(temp)):
                if ('"' in temp[i]):
                    # Until this point parser handled quote to look like this:
                    # [... '"Denver ', 'Broncos', '"']

                    # The following lines find where that is, removed all those items
                    # and replaces with the double_quote_string
                    for _ in range(0,3):
                        temp.pop(i)
                    temp.insert(i, double_quote_string)
                    break
            parsed_query = temp
    
        # Handles inputs with quotes that is only one word, ex "Football" is replaced with Football
        for i in range(0, len(parsed_query)):
            if ('"' in parsed_query[i]):
                temp_item = parsed_query[i].strip('"')
                parsed_query.pop(i)
                parsed_query.insert(i, temp_item)

        return parsed_query
    
    def double_quote(self, query_string):
        """
        Extracts the word or words from inside the double quotes

        :param query_string: raw string of the query
        :return double_quote_string: all the chars inside the double quotes
        """
    
        double_quote_string = ""
        quote_count = 0
        for char in query_string:

            # Once first quote is found add everything following 
            # to double_quote_string
            # When secound quote found stop
            if (char == '"'):
                quote_count += 1
            elif (quote_count == 1):
                double_quote_string += char

        # Verify that there is two words by checking there is a space followed by a char, 
        # if not return empty string
        if re.search(r'\s\w', double_quote_string):
            return double_quote_string
        return ""

    
