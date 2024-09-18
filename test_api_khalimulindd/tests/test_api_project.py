import pytest
import allure

CREATE_DATA_BODY_POSTS = {
    "data": {
        "year": 2024,
        "price": 4424.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}


NAMES = ["Huawei", "Samsung", "Apple"]


# Тест для создания трех постов и их удаление
@allure.feature('Create posts')
@allure.story('Implementation of posts')
@allure.title('Создание поста (POST)')
@allure.description(f'Данный тест выполняет создание поста с параметризацией и постусловием')
@pytest.mark.parametrize('name', NAMES)
def test_create_posts(create_post_endpoint, delete_post_endpoint, name):
    # Создаем копию словаря из списка
    body = CREATE_DATA_BODY_POSTS.copy()
    body["name"] = name

    # Создание поста
    create_post_endpoint.create_new_post(payload=body)

    # Проверка созданного поста
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_response_name_is_correct(name)

    # Получение ID созданного поста
    created_post_id = create_post_endpoint.post_id

    # Удаление поста
    delete_post_endpoint.delete_post(created_post_id)
    delete_post_endpoint.check_that_status_is_200()
    delete_post_endpoint.check_that_post_id_in_massage(created_post_id)


# Тест для создания одного поста с фиксированным именем

CREATE_DATA_BODY_POST = {
    "name": "Motorolla",
    "data": {
        "year": 4343,
        "price": 4314.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}


@allure.feature('Create posts')
@allure.story('Implementation of posts')
@allure.title('Создание одного поста (POST)')
@allure.description('Данный тест выполняет создание одного поста и его удаление')
def test_create_single_post(create_post_endpoint, delete_post_endpoint):
    # Создание поста
    create_post_endpoint.create_new_post(payload=CREATE_DATA_BODY_POST)
    name = create_post_endpoint.response.json()["name"]

    # Проверка созданного поста
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_response_name_is_correct(name)

    # Получение ID созданного поста
    created_post_id = create_post_endpoint.post_id

    # Удаление поста
    delete_post_endpoint.delete_post(created_post_id)
    delete_post_endpoint.check_that_status_is_200()
    delete_post_endpoint.check_that_post_id_in_massage(created_post_id)


# Тест для изменения поста методом PUT

UPDATE_DATA_BODY = {
    "name": "Oppo",
    "data": {
        "year": 3232,
        "price": 1111.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}


def test_update_post(create_post_endpoint, delete_post_endpoint, update_post_endpoint):

    # Создание поста
    create_post_endpoint.create_new_post(payload=CREATE_DATA_BODY_POST)

    # Получение ID созданного поста
    created_new_post_id = create_post_endpoint.post_id

    # Изменение поста
    update_post_endpoint.update_post(created_new_post_id, payload=UPDATE_DATA_BODY)
    updated_name = update_post_endpoint.response.json()["name"]

    # Проверка измененного поста
    update_post_endpoint.check_that_status_is_200()
    update_post_endpoint.check_response_name_is_correct(updated_name)

    # Получение ID измененного поста
    update_post_id = update_post_endpoint.update_post_id

    # Удаление измененного поста
    update_post_endpoint.update_post(update_post_id)
    update_post_endpoint.check_that_status_is_200()
    update_post_endpoint.check_that_post_id_in_massage(update_post_id)
