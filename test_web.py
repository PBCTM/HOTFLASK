from fastapi.testclient import TestClient
from web import api


client=TestClient(app=api)

def test1():
    output=client.get(url="/test")
    print(output.json(),output.status_code)
    assert output.json() == "Test was successful"
    assert output.status_code == 200

def test2():
    output=client.post(url="/sum",json={"a": 5, "b":9})
    print(output.json(),output.status_code)
    assert output.json() == 14.0
    assert output.status_code == 209

def test3():
    output=client.post(url="/sum",json={"a": 50, "b":9})
    print(output.json(),output.status_code)
    assert output.json() == 59.0
    assert output.status_code == 209