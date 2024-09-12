import requests


# Создание обьекта
def create_object():
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
    object_id = response.json()['id']
    return object_id


# ----------------------------------------------------------------------------------------------------


# Изменение обьекта методом PUT
def update_object_put(object_id):
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
        f'https://api.restful-api.dev/objects/{object_id}',
        json=body,
        headers=headers
    )
    print(response.json())
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Honor 80'
    update_object_put_id = response.json()['id']
    return update_object_put_id


# ----------------------------------------------------------------------------------------------------


# Изменение обьекта методом PATCH
def update_object_patch(object_id):
    body = {
        "name": "Iphone"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{object_id}',
        json=body,
        headers=headers
    )
    print(response.json())
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Iphone'
    update_object_patch_id = response.json()['id']
    return update_object_patch_id


# ----------------------------------------------------------------------------------------------------


# Удаление обьекта №4
def clear_object(object_id):
    delete_response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
    assert delete_response.status_code == 200, 'Status code is incorrect'
    assert delete_response.json()['message'] == f'Object with id = {object_id} has been deleted.'
    print(delete_response.json())


# Основная логика

# Создание объекта
created_object_id = create_object()

# Изменение объекта с помощью PUT
updated_object_put_id = update_object_put(created_object_id)

# Изменение объекта с помощью PATCH
updated_object_patch_id = update_object_patch(updated_object_put_id)

# Удаление объекта
clear_object(updated_object_patch_id)
