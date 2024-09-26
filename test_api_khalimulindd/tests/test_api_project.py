import pytest
import allure
from endpoints import create_product

# Создание экземпляра класса CreateObject
create_product_instance = create_product.CreateProduct()

# Переменные для работы создания продуктов с параметризацией
DATA_BODY_NO_NAME = create_product_instance.data_body_is_not_title()
TITLES = create_product_instance.generate_random_title()


# Тест для создания трех продуктов
@allure.feature('Create product')
@allure.story('Implementation of products')
@allure.title('Создание продукта с параметризацией')
@allure.description('Данный тест выполняет создание продукта с параметризацией')
@pytest.mark.parametrize('title', TITLES)
def test_create_product_with_param(create_product_endpoint, cleanup_product_fixture, request, title):
    # Генерация тела запроса с параметризированным именем
    body = DATA_BODY_NO_NAME
    body["title"] = title

    # Создание продукта
    request.function.product_id = create_product_endpoint.create_new_product(payload=body)

    # Проверка созданного продукта
    create_product_endpoint.check_that_status_is_200()


# Тест для изменения продукта методом PUT
@allure.feature('Update product')
@allure.story('Implementation of products')
@allure.title('Изменение продукта (PUT)')
@allure.description('Данный тест выполняет проверку изменение продукта')
def test_update_product_put(create_and_product_fixture, update_product_put_endpoint):
    update_put_body = {
        "title": "Harry Poter",
        "price": 13.5,
        "description": "lorem ipsum set",
        "image": "https://i.pravatar.cc",
        "category": "electronic"
    }

    # Изменение продукта
    update_product_put_endpoint.update_product_put(create_and_product_fixture, payload=update_put_body)

    # Проверка ответа после обновления
    update_product_put_endpoint.check_that_status_is_200()
    update_product_put_endpoint.check_response_title_is_correct(update_put_body['title'])


# Тест для изменения продукта методом PATCH
@allure.feature('Update product')
@allure.story('Implementation of products')
@allure.title('Изменение продукта (PATCH)')
@allure.description('Данный тест выполняет частичное изменение продукта')
def test_update_product_patch(create_and_product_fixture, update_product_patch_endpoint):
    update_patch_body = {
        "title": "Harison Ford"
    }

    # Изменение продукта
    update_product_patch_endpoint.update_product_patch(create_and_product_fixture, payload=update_patch_body)

    # Проверка ответа после обновления
    update_product_patch_endpoint.check_that_status_is_200()
    update_product_patch_endpoint.check_response_title_is_correct(update_patch_body['title'])


# Тест для удаление продукта
@allure.feature('Delete product')
@allure.story('Implementation of products')
@allure.title('Удаление продукта')
@allure.description('Данный тест выполняет удаление продукта')
def test_delete_product(create_product_fixture, delete_product_endpoint):

    # Удаляем продукта
    delete_product_endpoint.delete_product(created_product_id=create_product_fixture)

    # Проверка ответа после удаления
    delete_product_endpoint.check_that_status_is_200()
