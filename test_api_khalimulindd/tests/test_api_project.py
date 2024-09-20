import pytest
import allure
from endpoints import create_post


'''Генерируем тело ответа через функцию и заносим в переменную'''
DATA_BODY = create_post.CreatePost.generate_random_data_body()
DATA_BODY_NO_NAME = create_post.CreatePost.generate_random_base_data_body()
NAMES = create_post.CreatePost.generate_random_names()


# Тест для создания трех постов и их удаление
@allure.feature('Create posts')
@allure.story('Implementation of posts')
@allure.title('Создание поста с параметризацией')
@allure.description('Данный тест выполняет создание поста с параметризацией и постусловием')
@pytest.mark.parametrize('name', NAMES)
def test_create_posts_with_param(create_and_cleanup_post, cleanup_post_fixture, name):
    # Генерация тела запроса с параметризированным именем
    body = DATA_BODY_NO_NAME
    body["name"] = name

    # Создание поста
    create_and_cleanup_post.create_new_post(payload=body)

    # Проверка созданного поста
    create_and_cleanup_post.check_that_status_is_200()
    create_and_cleanup_post.check_response_name_is_correct(name)


# Тест для создания одного поста с фиксированным именем
@allure.feature('Create posts')
@allure.story('Implementation of posts')
@allure.title('Создание одного поста (POST)')
@allure.description('Данный тест выполняет проверку созданного поста')
def test_create_single_post(create_and_cleanup_post, create_post_endpoint):

    name = create_post_endpoint.response.json()["name"]

    # Проверка созданного поста
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_response_name_is_correct(name)


# Тест для изменения поста методом PUT
@allure.feature('Update posts')
@allure.story('Implementation of posts')
@allure.title('Изменение поста (PUT)')
@allure.description('Данный тест выполняет предварительно создание поста, изменение поста и его удаление')
def test_update_post_put(create_and_cleanup_post, update_post_put_endpoint):

    # Получение ID созданного поста
    created_new_post_id = create_and_cleanup_post.post_id

    # Изменение поста
    update_post_put_endpoint.update_post(
        created_new_post_id, payload=DATA_BODY
    )

    # Получение имени из обновленного поста
    updated_name = update_post_put_endpoint.response.json()["name"]

    # Проверка корректности имени после обновления
    update_post_put_endpoint.check_that_status_is_200()
    update_post_put_endpoint.check_response_name_is_correct(updated_name)


# Тест для изменения поста методом PATCH
@allure.feature('Update posts')
@allure.story('Implementation of posts')
@allure.title('Изменение поста (PATCH)')
@allure.description('Данный тест выполняет предварительно создание поста, частичное изменение поста и его удаление')
def test_update_post_patch(create_and_cleanup_post, update_post_patch_endpoint):

    # Получение ID созданного поста
    created_new_post_id = create_and_cleanup_post.post_id

    # Частичное изменение поста
    update_post_patch_endpoint.update_post_patch(created_new_post_id, payload=DATA_BODY_NO_NAME)

    # Получение имени из обновленного поста
    updated_name = update_post_patch_endpoint.response.json()["name"]

    # Проверка корректности имени после обновления
    update_post_patch_endpoint.check_that_status_is_200()
    update_post_patch_endpoint.check_response_name_is_correct(updated_name)


@allure.feature('Delete posts')
@allure.story('Implementation of posts')
@allure.title('Удаление поста')
@allure.description('Данный тест выполняет предварительно создание поста и его удаление')
def test_delete_post(create_post_fixture, cleanup_post_fixture, delete_post_endpoint):
    # Получение ID созданного поста
    created_new_post_id = create_post_fixture.post_id

    # Удаляем пост
    cleanup_post_fixture(created_new_post_id)

    # Проверяем, что пост был удалён
    delete_post_endpoint.check_that_status_is_200()
    delete_post_endpoint.check_that_post_id_in_massage(created_new_post_id)
