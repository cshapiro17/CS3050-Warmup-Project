import Firebase
firebase = Firebase.Firebase()

import parser_1
parser = parser_1.Parser()

# print(firebase.retrieve_all_data())

# Test the functionality of the program
run_program = True

while(run_program == True):
    parser_input = firebase.get_query_from_user()

    #print(parser_input)

    if (parser_input == "quit"):
        run_program = False
        continue

    parsed_query = parser.parse_query(parser_input)

    # print(parsed_query)

    output = firebase.process_query(parsed_query)

    print(output)