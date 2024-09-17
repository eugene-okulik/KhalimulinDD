import requests
import pytest
import allure


# Создание объекта трех обьектов
@allure.feature('Create posts')
@allure.story('Implementation of posts')
@allure.title('Создание трех постов (POST)')
@allure.description('Данный тест выполняет создание трех постов и после создания удаляет их')
@pytest.mark.parametrize('name', ['Iphone', 'Honor 51', 'Samsung'])
def test_creating_three(name, session_1, fun_1):
    with allure.step('Params request'):
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
    with allure.step('Sending a request'):
        response = requests.post(
            'https://api.restful-api.dev/objects',
            json=body,
            headers=headers
        )
    post_id = response.json()['id']
    with allure.step('Response code 200 received'):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step(f'The response body contains a name {name}'):
        assert response.json()['name'] == name
    print(f"\nСоздание объекта с ID: {post_id}")

    # Удаляем объекты после завершения теста
    print(f"\nУдаление объекта с ID: {post_id}")
    with allure.step('Deleting a post'):
        requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


# ----------------------------------------------------------------------------------------------------


# Изменение объекта методом PUT
@allure.feature('Change post by method PUT')
@allure.story('Implementation of posts')
@allure.title('Изменение поста (PUT)')
@allure.description('Данный тест выполняет изменение поста методом PUT.\n'
                    'Предусловие и постусловие выполняется с помощью фикстуры create_deleted')
@pytest.mark.medium
def test_update_object_put(create_deleted, fun_1):
    with allure.step('Params request'):
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
    with allure.step('Sending a request'):
        response = requests.put(
            f'https://api.restful-api.dev/objects/{create_deleted}',
            json=body,
            headers=headers
        )
    print(f"Обновлен объект (PUT): {response.json()}")
    with allure.step('Response code 200 received'):
        assert response.status_code == 200
    with allure.step(f'The response body contains a name Honor 80'):
        assert response.json()['name'] == 'Honor 80'


# ----------------------------------------------------------------------------------------------------

# Изменение объекта методом PATCH
@allure.feature('Change post by method PATCH')
@allure.story('Implementation of posts')
@allure.title('Изменение поста (PATCH)')
@allure.description('Данный тест выполняет изменение поста методом PATCH.\n'
                    'Предусловие и постусловие выполняется с помощью фикстуры create_deleted')
@pytest.mark.critical
def test_update_object_patch(create_deleted, fun_1):
    with allure.step('Params request'):
        body = {
            "name": "Iphone"
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Sending a request'):
        response = requests.patch(
            f'https://api.restful-api.dev/objects/{create_deleted}',
            json=body,
            headers=headers
        )
    print(f"Обновлен объект (PATCH): {response.json()}")
    with allure.step('Response code 200 received'):
        assert response.status_code == 200
    with allure.step(f'The response body contains a name Iphone'):
        assert response.json()['name'] == 'Iphone'


# ----------------------------------------------------------------------------------------------------


# Удаление объекта после создания
@allure.feature('Deleted post')
@allure.story('Implementation of posts')
@allure.title('Удаление поста (DELETE)')
@allure.description('Данный тест выполняет удаление поста.\n'
                    'Предусловие выполняется с помощью фикстуры creating_post_delete')
def test_delete_object(creating_post_delete, fun_1):
    with allure.step('Sending a request'):
        delete_response = requests.delete(f'https://api.restful-api.dev/objects/{creating_post_delete}')
    with allure.step('Response code 200 received'):
        assert delete_response.status_code == 200, 'Status code is incorrect'
    with allure.step(f'Checking that there is a remote ID in the massage field {creating_post_delete}'):
        assert delete_response.json()['message'] == f'Object with id = {creating_post_delete} has been deleted.'
    print(f"\nУдаление объекта с ID: {creating_post_delete}")
