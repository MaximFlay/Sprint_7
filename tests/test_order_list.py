import requests
import allure
from urls import BASE_URL, GET_ORDER_LIST_URL

class TestOrderList:

    @allure.title('Проверка получения списка заказов')
    def test_get_order_list(self):
        payload = {'nearestStation': '["1", "2"]'}
        response = requests.get(f'{BASE_URL}{GET_ORDER_LIST_URL}', params=payload)
        assert response.status_code == 200
        response_body = response.json()['orders']
        assert isinstance(response_body, list)
