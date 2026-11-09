import allure
import pytest

from data import ErrorMessages
from helpers import create_courier, generate_random_string


class TestCreateCourier:

    @allure.title('Курьера можно создать')
    def test_create_courier_success(self, courier_payload):
        response = create_courier(courier_payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_two_identical_couriers_conflict(self, courier_payload):
        create_courier(courier_payload)

        response = create_courier(courier_payload)

        assert response.status_code == 409
        assert response.json()["code"] == 409
        assert response.json()["message"] == ErrorMessages.LOGIN_ALREADY_IN_USE

    @allure.title('Нельзя создать курьера с логином, который уже есть')
    def test_create_courier_with_existing_login_conflict(self, courier):
        payload = {
            "login": courier[0],
            "password": generate_random_string(),
            "firstName": generate_random_string()
        }

        response = create_courier(payload)

        assert response.status_code == 409
        assert response.json()["code"] == 409
        assert response.json()["message"] == ErrorMessages.LOGIN_ALREADY_IN_USE

    @allure.title('Нельзя создать курьера без обязательного поля: {missing_field}')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_without_required_field_bad_request(self, courier_payload, missing_field):
        payload = dict(courier_payload)
        payload.pop(missing_field)

        response = create_courier(payload)

        assert response.status_code == 400
        assert response.json()["code"] == 400
        assert response.json()["message"] == ErrorMessages.CREATE_NOT_ENOUGH_DATA
