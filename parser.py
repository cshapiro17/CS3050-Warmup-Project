from pyparsing import Word, alphas, printables, ZeroOrMore, Suppress

def parseQuery(query_string):
    #define parsers for words and characters
    word_parser = Word(alphas)
    char_parser = Word(printables, excludeChars=" ")

    #define a parser for one or more words or characters
    sentence_parser = ZeroOrMore(word_parser | char_parser)

    #parse the query
    parsed_query = sentence_parser.parseString(query_string)


    return parsed_query

if __name__ == "__main__":
    query = input('Enter query:')

    #parse the query separated a the spaces
    result = parseQuery(query)

    print(result)