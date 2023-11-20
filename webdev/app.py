import requests

response = requests.get('https://www.python.org/')
print("Response: " + str({}) + str(response.status_code))
