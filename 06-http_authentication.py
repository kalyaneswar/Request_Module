import requests
from requests.auth import HTTPBasicAuth

r = requests.get("https://httpbin.org/basic-auth/user/passwd", auth=HTTPBasicAuth('username', 'password'))
print(r)
r = requests.get("https://httpbin.org/basic-auth/user/passwd", auth=HTTPBasicAuth('user', 'passwd'))
print(r)