import Firebase

firebase = Firebase.Firebase()

# print(firebase.retrieve_all_data())

# print(firebase.process_query("Sport", "==", "Football"))

firebase.process_query("Sport", "==", "Football")