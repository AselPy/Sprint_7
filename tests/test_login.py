import allure
import pytest

from data import ErrorMessages
from helpers import login_courier, generate_random_string


class TestLoginCourier:

    @allure.title('Курьер может авторизоваться, успешный запрос возвращает id')
    def test_login_courier_success(self, courier):
        response = login_courier({"login": courier[0], "password": courier[1]})

        assert response.status_code == 200
        assert isinstance(response.json()["id"], int)

    # Поле передаётся пустым, а не удаляется: без поля password сервер зависает (известный баг стенда)
    @allure.title('Нельзя авторизоваться без обязательного поля: {empty_field}')
    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_login_without_required_field_bad_request(self, courier, empty_field):
        payload = {"login": courier[0], "password": courier[1]}
        payload[empty_field] = ''

        response = login_courier(payload)

        assert response.status_code == 400
        assert response.json()["code"] == 400
        assert response.json()["message"] == ErrorMessages.LOGIN_NOT_ENOUGH_DATA

    @allure.title('Ошибка при неправильном поле: {wrong_field}')
    @pytest.mark.parametrize('wrong_field', ['login', 'password'])
    def test_login_with_wrong_credentials_not_found(self, courier, wrong_field):
        payload = {"login": courier[0], "password": courier[1]}
        payload[wrong_field] = generate_random_string()

        response = login_courier(payload)

        assert response.status_code == 404
        assert response.json()["code"] == 404
        assert response.json()["message"] == ErrorMessages.ACCOUNT_NOT_FOUND

    @allure.title('Ошибка при авторизации под несуществующим пользователем')
    def test_login_nonexistent_courier_not_found(self):
        payload = {"login": generate_random_string(), "password": generate_random_string()}

        response = login_courier(payload)

        assert response.status_code == 404
        assert response.json()["code"] == 404
        assert response.json()["message"] == ErrorMessages.ACCOUNT_NOT_FOUND
