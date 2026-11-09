import allure
import pytest

from data import ORDER_COLORS
from helpers import build_order_payload, create_order


class TestCreateOrder:

    @allure.title('Создание заказа с цветом: {color}')
    @pytest.mark.parametrize('color', ORDER_COLORS, ids=['black', 'grey', 'black_and_grey', 'no_color'])
    def test_create_order_with_color_returns_track(self, order_tracks, color):
        response = create_order(build_order_payload(color))

        assert response.status_code == 201
        track = response.json()["track"]
        order_tracks.append(track)
        assert isinstance(track, int)
