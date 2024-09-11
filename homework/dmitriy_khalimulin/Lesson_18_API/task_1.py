import requests


# Создание обьекта №1
def create_object_1():
    body = {
        "name": "Honor 10",
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
    print(response.json())
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Honor 10'
    object_id_1 = response.json()['id']
    return object_id_1


# Очистка обьекта №1 после создания
def clear_object_1(object_id_1):
    delete_response = requests.delete(f'https://api.restful-api.dev/objects/{object_id_1}')
    print(delete_response.json())


clear_object_1(create_object_1())


# ----------------------------------------------------------------------------------------------------


# Создание обьекта №2
def create_object_2():
    body = {
        "name": "Honor 50",
        "data": {
            "year": 3232,
            "price": 3334.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    print(response.json())
    object_id_2 = response.json()['id']
    return object_id_2


# Изменение обьекта №2 методом PUT
def update_object_2(object_id_2):
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
        f'https://api.restful-api.dev/objects/{object_id_2}',
        json=body,
        headers=headers
    )
    print(response.json())
    # assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Honor 80'
    update_object_id_2 = response.json()['id']
    return update_object_id_2


# Очистка обьекта №2 после изменения
def clear_object_2(update_object_id_2):
    delete_response = requests.delete(f'https://api.restful-api.dev/objects/{update_object_id_2}')
    print(delete_response.json())


clear_object_2(update_object_2(create_object_2()))


# ----------------------------------------------------------------------------------------------------


# Создание обьекта №3
def create_object_3():
    body = {
        "name": "Samsung",
        "data": {
            "year": 3332,
            "price": 331134.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    print(response.json())
    object_id_3 = response.json()['id']
    return object_id_3


# Изменение обьекта №3 методом PATCH
def update_object_3(object_id_3):
    body = {
        "name": "Iphone"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{object_id_3}',
        json=body,
        headers=headers
    )
    print(response.json())
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Iphone'
    update_object_id_3 = response.json()['id']
    return update_object_id_3


# Очистка обьекта №3 после изменения
def clear_object_3(update_object_id_3):
    delete_response = requests.delete(f'https://api.restful-api.dev/objects/{update_object_id_3}')
    print(delete_response.json())


clear_object_3(update_object_3(create_object_3()))


# ----------------------------------------------------------------------------------------------------


# Создание обьекта №4 для удаления
def create_object_4():
    body = {
        "name": "Oppo",
        "data": {
            "year": 3333,
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
    print(response.json())
    object_id_4 = response.json()['id']
    return object_id_4


# Удаление обьекта №4
def clear_object_4(object_id_4):
    delete_response = requests.delete(f'https://api.restful-api.dev/objects/{object_id_4}')
    assert delete_response.status_code == 200, 'Status code is incorrect'
    assert delete_response.json()['message'] == f'Object with id = {object_id_4} has been deleted.'
    print(delete_response.json())


clear_object_4(create_object_4())
