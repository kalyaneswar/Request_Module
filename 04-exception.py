import requests

try:
    r = requests.get("https://msabnaskdjbfkjsbgk.com")
except requests.exceptions.ConnectionError:
    print("CONNECTION ERROR")
