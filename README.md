# Sprint_7 — Автоматизация тестирования API сервиса «Самокат»

## Описание проекта

Проект содержит автотесты API сервиса «Самокат»: создание и логин курьера, создание заказа, список заказов.

## Используемые технологии

- Python
- Pytest
- Requests
- Allure

## Структура проекта

- `tests/` — автотесты API, для каждой ручки свой класс.
- `conftest.py` — фикстуры: создание и удаление тестовых курьеров, отмена созданных заказов.
- `helpers.py` — запросы к API и генерация тестовых данных.
- `data.py` — тестовые данные и тексты ошибок.
- `urls.py` — адреса API.
- `requirements.txt` — зависимости проекта.

## Запуск тестов

Установка зависимостей:

```bash
py -m pip install -r requirements.txt
```

Запуск всех тестов:

```bash
py -m pytest -v
```

## Создание отчёта Allure

```bash
py -m pytest --alluredir=target/allure-results
allure serve target/allure-results
```
