import requests
import allure
from urls import BASE_URL, LOGIN_COURIERS_URL
from conftest import create_and_delete_courier
class TestLoginCourier:

    @allure.title("Проверка авторизации курьера и возвращения в ответе id. Все обязательные поля заполнены валидными данными")
    def test_login_courier(self, create_and_delete_courier):
        payload = {
            "login": create_and_delete_courier["login"],
            "password": create_and_delete_courier["password"]
        }

        response = requests.post(f'{BASE_URL}{LOGIN_COURIERS_URL}', data=payload)
        assert response.status_code == 200 and "id" in response.text


    @allure.title("Проверка, что система вернёт ошибку, если неправильно указать логин. Проверка, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    def test_login_courier_with_invalid_login(self, create_and_delete_courier):
        payload = {
            "login": create_and_delete_courier["password"],
            "password": create_and_delete_courier["password"]
        }

        response = requests.post(f'{BASE_URL}{LOGIN_COURIERS_URL}', data=payload)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"


    @allure.title("Проверка, что система вернёт ошибку, если неправильно ввести пароль")
    def test_login_courier_with_invalid_password(self, create_and_delete_courier):
        payload = {
            "login": create_and_delete_courier["login"],
            "password": create_and_delete_courier["login"]
        }

        response = requests.post(f'{BASE_URL}{LOGIN_COURIERS_URL}', data=payload)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"


    @allure.title("Проверка, что система вернёт ошибку, если не указать логин")
    def test_login_courier_without_login(self, create_and_delete_courier):
        payload = {
            "login": "",
            "password": create_and_delete_courier["password"]
        }

        response = requests.post(f'{BASE_URL}{LOGIN_COURIERS_URL}', data=payload)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"


    @allure.title("Проверка, что система вернёт ошибку, если не указать пароль")
    def test_login_courier_without_password(self, create_and_delete_courier):
        payload = {
            "login": create_and_delete_courier["login"],
            "password": ""
        }

        response = requests.post(f'{BASE_URL}{LOGIN_COURIERS_URL}', data=payload)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"