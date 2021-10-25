import requests
import pytest
import json
import jsonpath

    
def test_postjson():
    url_endpoint = 'http://api.noobtest.id/dummy/v1/users'
    
    file = open('D:\Code\CODING ID\API_TEST\post.json', 'r')
    
    req_json = json.loads(file.read())

    response = requests.post(url_endpoint, json=req_json)
    
    Code = response.status_code
    
    assert Code == 200
    
    json_response = json.loads(response.text)
    
    Name = jsonpath.jsonpath(json_response, 'name')
    
    assert Name[0] == 'Rapael'