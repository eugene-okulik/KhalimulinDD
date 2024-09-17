import requests
import pytest


# Фикстура для всей сессии
@pytest.fixture(scope='session')
def session_1():
    print('\nStart testing')
    yield
    print('Testing completed')


# Фикстура для функций
@pytest.fixture()
def fun_1():
    print('\nbefore test')
    yield
    print('\nafter test')


# Фикстура для создания и удаления объекта
@pytest.fixture()
def create_deleted():
    body = {
        "name": "Samsung",
        "data": {
            "year": 2024,
            "price": 4424.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']

    print(f"\nСоздан объект с ID: {post_id}")

    yield post_id

    # Удаляем объект после завершения теста
    print(f"\nУдаление объекта с ID: {post_id}")
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


# Фикстура создания обьекта
@pytest.fixture()
def creating_post_delete():
    body = {
        "name": "Oppo",
        "data": {
            "year": 2024,
            "price": 4424.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    post_delete_id = response.json()['id']
    print(f"\nСоздание объекта с ID: {post_delete_id}")
    return post_delete_id