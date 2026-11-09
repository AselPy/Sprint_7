import datetime
import random
import string

import allure
import requests

from data import ORDER_DATA
from urls import COURIER, LOGIN_COURIER, ORDERS, CANCEL_ORDER


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_courier_payload():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }


def build_order_payload(color):
    payload = dict(ORDER_DATA)
    payload["deliveryDate"] = (datetime.date.today() + datetime.timedelta(days=3)).isoformat()
    payload["color"] = color
    return payload


@allure.step('Создать курьера')
def create_courier(payload):
    return requests.post(COURIER, json=payload)


@allure.step('Авторизовать курьера')
def login_courier(payload):
    return requests.post(LOGIN_COURIER, json=payload)


@allure.step('Удалить курьера с id {courier_id}')
def delete_courier(courier_id):
    return requests.delete(f'{COURIER}/{courier_id}')


@allure.step('Удалить курьера по логину и паролю, если он существует')
def delete_courier_if_exists(login, password):
    response = login_courier({"login": login, "password": password})
    if response.status_code == 200:
        delete_courier(response.json()["id"])


@allure.step('Создать заказ')
def create_order(payload):
    return requests.post(ORDERS, json=payload)


@allure.step('Отменить заказ с треком {track}')
def cancel_order(track):
    return requests.put(CANCEL_ORDER, params={"track": track}, json={"track": track})


@allure.step('Получить список заказов')
def get_orders_list():
    return requests.get(ORDERS)


# Метод из задания: регистрирует нового курьера и возвращает [логин, пароль, имя].
# Если регистрация не удалась, возвращает пустой список.
def register_new_courier_and_return_login_password():
    login_pass = []
    payload = generate_courier_payload()

    response = create_courier(payload)

    if response.status_code == 201:
        login_pass.append(payload["login"])
        login_pass.append(payload["password"])
        login_pass.append(payload["firstName"])

    return login_pass
