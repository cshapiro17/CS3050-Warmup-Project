import json
from Firebase import *

# Connect to firebase
#connect()

# Load data
json_data = 'SmithAthletes.json'

with open(json_data) as f:
    smithAthletes = json.load(f)

# Add credentials to make connection
cred = credentials.Certificate("smithathletes-d8741-firebase-adminsdk-snc4k-3e47fd0006.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://smithathletes-d8741-default-rtdb.firebaseio.com/"})

# Database 
db = firestore.client()
collection_ref = db.collection('SmithAthletes')

# Iterate through the JSON data and update the documents in the collection
for item in smithAthletes:
    # Use the 'Unique id' as the document ID
    unique_id = str(item['Unique id'])
    doc_ref = collection_ref.document(unique_id)
    # Set the document with the rest of the data
    doc_ref.set(item)


# Guessing from here we parse json and upload to firebase in a loop?


