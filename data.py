class ErrorMessages:
    CREATE_NOT_ENOUGH_DATA = 'Недостаточно данных для создания учетной записи'
    LOGIN_ALREADY_IN_USE = 'Этот логин уже используется. Попробуйте другой.'
    LOGIN_NOT_ENOUGH_DATA = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'


# Базовые данные заказа: цвет и дата доставки подставляются в helpers.build_order_payload
ORDER_DATA = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "Москва, улица Ленина, 1",
    "metroStation": 4,
    "phone": "+7 999 123 45 67",
    "rentTime": 5,
    "comment": "Позвонить перед доставкой"
}

ORDER_COLORS = [
    ['BLACK'],
    ['GREY'],
    ['BLACK', 'GREY'],
    []
]
