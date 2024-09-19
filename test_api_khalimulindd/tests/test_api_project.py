import pytest
import allure
from endpoints import create_post
from endpoints import update_post_put
from endpoints import update_post_patch


# Тест для создания трех постов и их удаление
@allure.feature('Create posts')
@allure.story('Implementation of posts')
@allure.title('Создание поста c параметризацией')
@allure.description(f'Данный тест выполняет создание поста с параметризацией и постусловием')
@pytest.mark.parametrize('name', create_post.CreatePost.generate_random_names())
def test_create_posts(create_post_endpoint, delete_post_endpoint, name):
    # Создаем копию словаря из списка
    body = create_post.CreatePost.generate_random_base_data_body()
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


# Тест для создания одного поста с фиксированным именем
@allure.feature('Create posts')
@allure.story('Implementation of posts')
@allure.title('Создание одного поста (POST)')
@allure.description('Данный тест выполняет создание одного поста и его удаление')
def test_create_single_post(create_post_endpoint, delete_post_endpoint):
    # Создание поста
    create_post_endpoint.create_new_post()
    name = create_post_endpoint.response.json()["name"]

    # Проверка созданного поста
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_response_name_is_correct(name)

    # Получение ID созданного поста
    created_post_id = create_post_endpoint.post_id

    # Удаление поста
    delete_post_endpoint.delete_post(created_post_id)


# Тест для изменения поста методом PUT

'''Генерируем тело ответа через функцию родительского файла и заносим в переменную'''
UPDATE_DATA_BODY = update_post_put.UpdatePostPut.generate_random_data_body()


@allure.feature('Update posts')
@allure.story('Implementation of posts')
@allure.title('Изменение поста (PUT)')
@allure.description('Данный тест выполняет предварительно создание поста, изменение поста и его удаление')
def test_update_post_put(create_post_endpoint, delete_post_endpoint, update_post_put_endpoint):
    # Создание поста
    create_post_endpoint.create_new_post()

    # Проверка успешного создания поста
    create_post_endpoint.check_that_status_is_200()

    # Получение ID созданного поста
    created_new_post_id = create_post_endpoint.post_id

    # Изменение поста
    update_post_put_endpoint.update_post(created_new_post_id, payload=UPDATE_DATA_BODY)

    # Получение имени из обновленного поста
    updated_name = update_post_put_endpoint.response.json()["name"]

    # Проверка корректности имени после обновления
    update_post_put_endpoint.check_that_status_is_200()
    update_post_put_endpoint.check_response_name_is_correct(updated_name)

    # Удаление измененного поста
    delete_post_endpoint.delete_post(created_new_post_id)


# Тест для изменения поста методом PATCH
@allure.feature('Update posts')
@allure.story('Implementation of posts')
@allure.title('Изменение поста (PATCH)')
@allure.description('Данный тест выполняет предварительно создание поста, частичное изменение поста и его удаление')
def test_update_post_patch(create_post_endpoint, delete_post_endpoint, update_post_patch_endpoint):

    body = update_post_patch.UpdatePostPatch.generate_random_base_data_body()

    # Создание поста
    create_post_endpoint.create_new_post()

    # Проверка успешного создания поста
    create_post_endpoint.check_that_status_is_200()

    # Получение ID созданного поста
    created_new_post_id = create_post_endpoint.post_id

    # Изменение поста
    update_post_patch_endpoint.update_post_patch(created_new_post_id, payload=body)

    # Получение имени из обновленного поста
    updated_name = update_post_patch_endpoint.response.json()["name"]

    # Проверка корректности имени после обновления
    update_post_patch_endpoint.check_that_status_is_200()
    update_post_patch_endpoint.check_response_name_is_correct(updated_name)

    # Удаление измененного поста
    delete_post_endpoint.delete_post(created_new_post_id)


#  Тест для удаления поста
@allure.feature('Delete posts')
@allure.story('Implementation of posts')
@allure.title('Удаление поста')
@allure.description('Данный тест выполняет предварительно создание поста и его удаление')
def test_delete_post(create_post_endpoint, delete_post_endpoint):
    # Создание поста
    create_post_endpoint.create_new_post()

    # Проверка созданного поста
    create_post_endpoint.check_that_status_is_200()

    # Получение ID созданного поста
    created_new_post_id = create_post_endpoint.post_id

    # Удаление поста
    delete_post_endpoint.delete_post(created_new_post_id)

    # Проверка ответа
    delete_post_endpoint.check_that_status_is_200()
    delete_post_endpoint.check_that_post_id_in_massage(created_new_post_id)
