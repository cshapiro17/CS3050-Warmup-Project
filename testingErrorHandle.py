import Firebase
import parser_1

parser = parser_1.Parser()
firebase = Firebase.Firebase()

# print(firebase.get_column_titles())

docs = firebase.retrieve_all_data()
dicttt = dict()
for item in docs:
    dicttt = item.to_dict()
print(col)

