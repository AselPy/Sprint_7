import allure

from helpers import get_orders_list


class TestOrdersList:

    @allure.title('В тело ответа возвращается список заказов')
    def test_get_orders_list_returns_orders(self):
        response = get_orders_list()

        assert response.status_code == 200
        orders = response.json()["orders"]
        assert isinstance(orders, list)
        assert len(orders) > 0
