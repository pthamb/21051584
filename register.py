import requests
import json

url = "http://20.244.56.144/test/register"
data = {
    "companyName": "neighborgood",
    "ownerName": "Purnendu",
    "rollNo": "21051584",
    "OwnerEmail": "21051584@kiit.ac.in",
    "accessCode": "mjPQGJ"
}

# response = requests.post(url, data=data)

# print(response.status_code)  
# print(response.text)         
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)  
print(response.text)         
