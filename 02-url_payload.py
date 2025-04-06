import requests


url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    'userId': 1
}
response = requests.get(url, params=payload)

print("Final URL:", response.url)
print("Data:", response.json())