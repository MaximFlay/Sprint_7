import requests
import random
import string
from urls import *

def register_new_courier_and_return_courier_data(login, password, first_name):
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{BASE_URL}{CREATE_COURIERS_URL}', data=payload)
    courier_data = response.json()

    if response.status_code == 201:
        courier_data["login"] = login
        courier_data["password"] = password
        courier_data["firstName"] = first_name

    return courier_data

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string

def generate_courier_data():
    courier_data = {}

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    courier_data["login"] = login
    courier_data["password"] = password
    courier_data["firstName"] = first_name

    return courier_data

def courier_login(login, password):
    payload = {"login": login, "password": password}
    response = requests.post(f"{BASE_URL}{LOGIN_COURIERS_URL}", data=payload)
    return response

def delete_courier(id):
    requests.delete(f"{BASE_URL}{DELETE_COURIERS_URL}{id}")
