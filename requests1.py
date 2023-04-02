import requests

response = requests.get("http://data.pr4e.org/romeo.txt")
print(response.text)