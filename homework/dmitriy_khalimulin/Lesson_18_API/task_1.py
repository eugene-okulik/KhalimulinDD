import requests


# Создание объекта
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
    print(f"Создан объект: {response.json()}")
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Honor 10'
    return response.json()['id']


# ----------------------------------------------------------------------------------------------------


# Изменение объекта методом PUT
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
    print(f"Обновлен объект (PUT): {response.json()}")
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Honor 80'


# ----------------------------------------------------------------------------------------------------


# Изменение объекта методом PATCH
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
    print(f"Обновлен объект (PATCH): {response.json()}")
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Iphone'


# ----------------------------------------------------------------------------------------------------


# Удаление объекта
def clear_object(object_id):
    delete_response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
    print(f"Удален объект: {delete_response.json()}")
    assert delete_response.status_code == 200, 'Status code is incorrect'
    assert delete_response.json()['message'] == f'Object with id = {object_id} has been deleted.'


# ----------------------------------------------------------------------------------------------------


def main():
    # Создание и удаление объекта
    object_id = create_object()
    clear_object(object_id)

    # Создание, изменение (PUT) и удаление объекта
    object_id = create_object()
    update_object_put(object_id)
    clear_object(object_id)

    # Создание, изменение (PATCH) и удаление объекта
    object_id = create_object()
    update_object_patch(object_id)
    clear_object(object_id)

    # Просто создание и удаление объекта
    object_id = create_object()
    clear_object(object_id)


main()
