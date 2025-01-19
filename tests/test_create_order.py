import json
import pytest
import requests
import allure
from urls import BASE_URL, CREATE_ORDER_URL
from data import OrderData

class TestCreateOrder:

    @allure.title('Проверка создания заказа')
    @allure.description('Проверка создания заказа с помощью параметризации, если выбран черный самокат, серый самокат, выбраны оба цвета, не выбран цвет')
    @pytest.mark.parametrize('order_data', [
        OrderData.order_data_1, OrderData.order_data_2,
        OrderData.order_data_3, OrderData.order_data_4
    ])
    def test_create_order(self, order_data):
        order_data = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{BASE_URL}{CREATE_ORDER_URL}', data=order_data, headers=headers)

        assert response.status_code == 201 and 'track' in response.text