import requests

url = "https://reqres.in/api/users"

payload = {
    "name": "Kalyan",
    "job": "DevOps Engineer"
}

response = requests.post(url, json=payload)

print(response)
print(response.text)