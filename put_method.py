import requests

url_endpoint = 'http://api.noobtest.id/dummy/v1/users/8'

query = {"email": "rapael826@mailist.com","name": "Maitimo"}

response = requests.put(url_endpoint, json=query)

print(response.status_code)
print(response.text)