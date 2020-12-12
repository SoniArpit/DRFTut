import requests
import json

URL = "http://127.0.0.1:8000/stuapi/2/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


def post_data():
    data = {"name": "Bruce", "roll": 108, "city": "Madhapar"}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


def update_data():
    data = {"name": "Tony", "roll": 208, "city": "Madhapar"}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


def delete_data():
    data = {"id": 3}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# get_data()
# post_data()
update_data()
# delete_data()
