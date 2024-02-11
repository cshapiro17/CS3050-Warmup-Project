import Firebase
import parser_1

parser = parser_1.Parser()
firebase = Firebase.Firebase()

print(firebase.get_column_titles())

