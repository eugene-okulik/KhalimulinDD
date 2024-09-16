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


# ----------------------------------------------------------------------------------------------------

# Создание объекта трех обьектов
@pytest.mark.parametrize('name', ['Iphone', 'Honor 51', 'Samsung'])
def test_creating_three(name, session_1, fun_1):
    body = {
        "name": name,
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
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == name
    print(f"\nСоздание объекта с ID: {post_id}")

    # Удаляем объекты после завершения теста
    print(f"\nУдаление объекта с ID: {post_id}")
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


# ----------------------------------------------------------------------------------------------------

# Изменение объекта методом PUT
@pytest.mark.medium
def test_update_object_put(create_deleted, fun_1):
    body = {
        "name": "Honor 80",
        "data": {
            "year": 2029,
            "price": 774.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{create_deleted}',
        json=body,
        headers=headers
    )
    print(f"Обновлен объект (PUT): {response.json()}")
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Honor 80'


# ----------------------------------------------------------------------------------------------------

# Изменение объекта методом PATCH
@pytest.mark.critical
def test_update_object_patch(create_deleted, fun_1):
    body = {
        "name": "Iphone"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{create_deleted}',
        json=body,
        headers=headers
    )
    print(f"Обновлен объект (PATCH): {response.json()}")
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Iphone'


# ----------------------------------------------------------------------------------------------------
# Фикстура создания обьекта для удаления
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


# Удаление объекта после создания
def test_delete_object(creating_post_delete, fun_1):
    delete_response = requests.delete(f'https://api.restful-api.dev/objects/{creating_post_delete}')
    assert delete_response.status_code == 200, 'Status code is incorrect'
    assert delete_response.json()['message'] == f'Object with id = {creating_post_delete} has been deleted.'
    print(f"\nУдаление объекта с ID: {creating_post_delete}")
