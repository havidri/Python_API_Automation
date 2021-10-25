import requests

url_endpoint = 'http://api.noobtest.id/dummy/v1/users'

response = requests.get(url_endpoint)

print(response.text)