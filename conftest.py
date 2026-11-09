import pytest

from helpers import (
    generate_courier_payload,
    register_new_courier_and_return_login_password,
    delete_courier_if_exists,
    cancel_order
)


@pytest.fixture
def courier():
    """Зарегистрированный курьер [логин, пароль, имя]; удаляется после теста."""
    courier_data = register_new_courier_and_return_login_password()
    assert courier_data, 'Не удалось создать тестового курьера'

    yield courier_data

    delete_courier_if_exists(courier_data[0], courier_data[1])


@pytest.fixture
def courier_payload():
    """Данные нового курьера (ещё не создан). Если тест его создаст — курьер удалится после теста."""
    payload = generate_courier_payload()

    yield payload

    delete_courier_if_exists(payload["login"], payload["password"])


@pytest.fixture
def order_tracks():
    """Список треков созданных в тесте заказов; все заказы отменяются после теста."""
    tracks = []

    yield tracks

    for track in tracks:
        cancel_order(track)
