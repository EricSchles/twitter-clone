import requests
from app import app



def test_index():
    assert requests.get("http://localhost:5000/").status_code == 200
    assert requests.get("http://localhost:5000/").text == requests.get("http://localhost:5000/index").text
    assert requests.get("http://localhost:5000/").text.lower() == "hello world" 

def test_whatever():
    assert requests.get("http://localhost:5000/whatever").status_code == 200
    assert requests.get("http://localhost:5000/whatever").text == requests.get("http://localhost:5000/index").text
    assert requests.get("http://localhost:5000/whatever").text.lower() == "whatever" 
    
def test_publish():
    assert requests.get("http://localhost:5000/publish", data={"posting": "Hello there"}).status_code == 200
    assert requests.get("http://localhost:5000/publish", data={"posting": "Hello there"}).text == "Hello there"
