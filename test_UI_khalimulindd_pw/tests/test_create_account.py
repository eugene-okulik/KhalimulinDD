import os
import pytest
import allure
import dotenv
from faker import Faker
from test_UI_khalimulindd_pw.pages.create_account_page import CreateAccount as CA

# Создаем объект Faker
fake = Faker()

# Используем dotenv
dotenv.load_dotenv()


@allure.feature('Create account')
@allure.story('Create new customer account')
@allure.title('Создание аккаунта')
@allure.description('Данный тест выполняет создание аккаунта с заполнением всех полей валидными данными')
@pytest.mark.smoke
def test_correct_create_account(create_account_page):

    # Открытие страницы в браузере
    create_account_page.open_page()

    # Заполнение формы создания аккаунта
    create_account_page.fill_customer_form(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password=os.getenv('PASSWORD'),
        confirm_password=os.getenv('PASSWORD')
    )

    # Проверка соответствующего текста после создания аккаунта
    create_account_page.check_text_after_creating_an_account(
        create_account_page.search_text_after_account_creation,
        create_account_page.text_to_check_the_created_account
    )


@allure.feature('Create account')
@allure.story('Create new customer account no required fields')
@allure.title('Попытка создания аккаунта без обязательных полей')
@allure.description('Этот тест проверяет попытку создания аккаунта при отсутствии обязательных полей')
@pytest.mark.smoke
@pytest.mark.parametrize(
    "field, first_name, last_name, email, password, confirm_password, error_message",
    CA.get_test_data_no_required_fields()
)
def test_create_account_no_required_fields(
        create_account_page, field, first_name, last_name, email, password, confirm_password, error_message
):
    # Открытие страницы в браузере
    create_account_page.open_page()

    # Заполнение формы, где одно поле пропущено
    create_account_page.fill_customer_form(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        confirm_password=confirm_password
    )

    # Проверка, что сообщение об ошибке отображается для конкретного поля
    create_account_page.check_field_error_is_displayed(field, error_message)
