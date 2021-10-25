import requests
import pytest
import json
import jsonpath

def test_getuser():
    url_endpoint = 'http://api.noobtest.id/dummy/v1/users/1'
    
    response = requests.get(url_endpoint)
    
    Code = response.status_code
    
    assert Code == 200
    
    json_response = json.loads(response.text)
    
    Name = jsonpath.jsonpath(json_response, 'name')
    
    assert Name[0] == 'broto'
    
def test_postuser():
    url_endpoint = 'http://api.noobtest.id/dummy/v1/users'
    
    query = {"email": "apitesting@mailist.com", "name": "API test"}
    
    response = requests.post(url_endpoint, json=query)
    
    Code = response.status_code
    
    assert Code == 200
    
    json_response = json.loads(response.text)
    
    Name = jsonpath.jsonpath(json_response, 'name')
    
    assert Name[0] == 'API test'