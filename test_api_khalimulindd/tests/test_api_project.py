import pytest
import allure
from endpoints import create_object

# Создание экземпляра класса CreateObject
create_obj_instance = create_object.CreateObject()

# Использование метода для генерации случайных данных
DATA_BODY = create_obj_instance.generate_random_data_body()
DATA_BODY_NO_NAME = create_obj_instance.generate_random_base_data_body()
NAMES = create_obj_instance.generate_random_names()


# Тест для создания трех обьектов
@allure.feature('Create object')
@allure.story('Implementation of objects')
@allure.title('Создание обьекта с параметризацией')
@allure.description('Данный тест выполняет создание обьекта с параметризацией и постусловием')
@pytest.mark.parametrize('name', NAMES)
def test_create_objects_with_param(create_object_fixture, cleanup_object_fixture, create_object_endpoint, name):
    # Генерация тела запроса с параметризированным именем
    body = DATA_BODY_NO_NAME
    body["name"] = name

    # Создание обьекта и получение его ID
    create_object_endpoint, created_object_id = create_object_fixture(payload=body)

    # Проверка созданного обьекта
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_name_is_correct(name)

    # Удаление обьекта после проверки
    cleanup_object_fixture(object_id=created_object_id)


# Тест для создания одного обьекта с фиксированным именем
@allure.feature('Create object')
@allure.story('Implementation of objects')
@allure.title('Создание одного обьекта (POST)')
@allure.description('Данный тест выполняет проверку созданного обьекта')
def test_create_single_object(create_object_fixture, cleanup_object_fixture, create_object_endpoint):

    # Создание обьекта и получение его ID
    create_object_endpoint, created_object_id, created_name = create_object_fixture(payload=None)

    # Проверка созданного обьекта
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_name_is_correct(created_name)

    # Удаление обьекта после проверки
    cleanup_object_fixture(object_id=created_object_id)


# Тест для изменения обьекта методом PUT
@allure.feature('Update object')
@allure.story('Implementation of objects')
@allure.title('Изменение обьекта (PUT)')
@allure.description('Данный тест выполняет проверку изменение обьекта')
def test_update_object_put(
        create_object_fixture, cleanup_object_fixture, update_object_put_endpoint, update_put_object_fixture
):

    # Создание обьекта и получение его ID
    create_object_endpoint, created_object_id = create_object_fixture(payload=None)

    # Изменение обьекта
    update_object_endpoint, update_object_id, update_object_name = update_put_object_fixture(
        created_object_id, payload=None
    )

    # Проверка ответа после обновления
    update_object_put_endpoint.check_that_status_is_200()
    update_object_put_endpoint.check_response_name_is_correct(update_object_name)

    # Удаление обновленного обьекта после проверки
    cleanup_object_fixture(object_id=update_object_id)


# Тест для изменения обьекта методом PATCH
@allure.feature('Update object')
@allure.story('Implementation of objects')
@allure.title('Изменение обьекта (PATCH)')
@allure.description('Данный тест выполняет частичное изменение поста')
def test_update_object_patch(
        create_object_fixture, cleanup_object_fixture, update_object_patch_endpoint, update_patch_object_fixture
):

    # Создание обьекта и получение его ID
    create_object_endpoint, created_object_id = create_object_fixture(payload=None)

    # Изменение обьекта
    update_object_endpoint, update_object_id, update_object_name = update_patch_object_fixture(
        created_object_id, payload=None
    )

    # Проверка ответа после обновления
    update_object_patch_endpoint.check_that_status_is_200()
    update_object_patch_endpoint.check_response_name_is_correct(update_object_name)

    # Удаление обновленного обьекта после проверки
    cleanup_object_fixture(object_id=update_object_id)


# Тест для удаление обьекта
@allure.feature('Delete object')
@allure.story('Implementation of objects')
@allure.title('Удаление обьекта')
@allure.description('Данный тест выполняет удаление обьекта')
def test_delete_object(create_object_fixture, cleanup_object_fixture, delete_object_endpoint):
    # Создание обьекта и получение его ID
    created_object_id = create_object_fixture(payload=None)

    # Удаляем обьект
    cleanup_object_fixture(object_id=created_object_id)

    # Проверяем, что обьект был удалён
    delete_object_endpoint.check_that_status_is_200()
    delete_object_endpoint.check_that_post_id_in_massage(created_object_id)
