import pytest
from helpers import *

@pytest.fixture(scope="function")
def create_and_delete_courier():
    courier_data = generate_courier_data()
    courier = register_new_courier_and_return_courier_data(courier_data['login'], courier_data['password'], courier_data['firstName'])
    courier_id = courier_login(courier["login"], courier["password"]).json()["id"]
    yield courier
    delete_courier(courier_id)