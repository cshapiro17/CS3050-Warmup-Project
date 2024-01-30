import json
from FirebaseConnection import *

# Connect to firebase
#connect()

# Load data
json_data = 'SmithAthletes - Sheet1.json'

with open(json_data) as f:
    smithAthletes = json.load(f)

print(smithAthletes)


