import requests

try:
    r = requests.get("https://httpbin.org/", timeout=0.00001)
except requests.exceptions.ConnectTimeout:
    print("Timed out")