import json
from FirebaseConnection import *

# Connect to firebase
#connect()

# Load data
json_data = 'SmithAthletes.json'

with open(json_data) as f:
    smithAthletes = json.load(f)

# Test
print(smithAthletes)

# Guessing from here we parse json and upload to firebase in a loop?


