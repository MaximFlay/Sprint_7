import requests
import allure
from urls import BASE_URL, CREATE_COURIERS_URL
from helpers import generate_courier_data

class TestCreateCourier:

    @allure.title('Проверка создания курьера. Все поля заполнены валидными данными')
    def test_create_courier_all_fields_are_filled(self):
        courier_data = generate_courier_data()
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }
        response = requests.post(f'{BASE_URL}{CREATE_COURIERS_URL}', data=payload)

        assert response.status_code == 201 and response.json() == {'ok': True}


    @allure.title('Проверка создания курьера. Все обязательные поля заполнены валидными данными')
    def test_create_courier_all_required_fields_are_filled(self):
        courier_data = generate_courier_data()
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": ""
        }
        response = requests.post(f'{BASE_URL}{CREATE_COURIERS_URL}', data=payload)

        assert response.status_code == 201 and response.json() == {'ok': True}


    @allure.title('Проверка отсутствия возможности создания курьера с одинаковыми данными')
    def test_create_courier_with_the_same_data(self):
        courier_data = generate_courier_data()
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }
        requests.post(f'{BASE_URL}{CREATE_COURIERS_URL}', data=payload)
        response_courier_2 = requests.post(f'{BASE_URL}{CREATE_COURIERS_URL}', data=payload)
        assert response_courier_2.status_code == 409 and response_courier_2.json()["message"] == "Этот логин уже используется. Попробуйте другой."


    @allure.title('Проверка, что если отсутствует поле "login", возвращается ошибка')
    def test_create_courier_without_login(self):
        courier_data = generate_courier_data()
        payload = {
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }
        response = requests.post(f'{BASE_URL}{CREATE_COURIERS_URL}', data=payload)

        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"


    @allure.title('Проверка, что если отсутствует поле "password", возвращается ошибка')
    def test_create_courier_without_password(self):
        courier_data = generate_courier_data()
        payload = {
            "login": courier_data["login"],
            "firstName": courier_data["firstName"]
        }
        response = requests.post(f'{BASE_URL}{CREATE_COURIERS_URL}', data=payload)

        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"


    @allure.title('Проверка, что если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_create_courier_duplicate_login(self):
        courier_data_1 = generate_courier_data()
        payload = {
            "login": courier_data_1["login"],
            "password": courier_data_1["password"],
            "firstName": courier_data_1["firstName"]
        }
        response_courier_1 = requests.post(f'{BASE_URL}{CREATE_COURIERS_URL}', data=payload)
        assert response_courier_1.status_code == 201 and response_courier_1.json() == {'ok': True}

        courier_data_2 = generate_courier_data()
        payload = {
            "login": courier_data_1["login"],
            "password": courier_data_2["password"],
            "firstName": courier_data_2["firstName"]
        }

        response_courier_2 = requests.post(f'{BASE_URL}{CREATE_COURIERS_URL}', data=payload)
        assert response_courier_2.status_code == 409 and response_courier_2.json()["message"] == "Этот логин уже используется. Попробуйте другой."