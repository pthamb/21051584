import requests
import json

# API endpoint
url = "http://20.244.56.144/test/auth"

# Data to be sent to API
data = {
    "companyName": "neighborgood",
    "clientID":"6c3b94eb-9c4e-49db-9577-d4b49c47dc56",
    "clientSecret":"lhdLfSVupjmBQOgg",
    "ownerName": "Purnendu",
    "rollNo": "21051584",
    "OwnerEmail": "21051584@kiit.ac.in",
    "accessCode": "mjPQGJ"
}

# Set the headers to specify JSON content type
headers = {'Content-Type': 'application/json'}

# Send POST request with JSON data
response = requests.post(url, data=json.dumps(data), headers=headers)

# Print the status code and response data
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
