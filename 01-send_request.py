import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.status_code)
# print(response.text)


response = requests.get("https://reqres.in/api/users/2")
print(response.text)