import pytest
import allure


@allure.feature('Adding a product to the cart')
@allure.story('Adding a product')
@allure.title('Добавление товара в корзину')
@allure.description('Этот тест добавляет товар в корзину и проверяет что товар добавлен')
@pytest.mark.smoke
def test_adding_a_product_to_the_cart(sale_page):

    # Открытие страницы в браузере
    sale_page.open_page()

    # Добавление и открытие корзины
    sale_page.adding_sixth_product_to_cart()

    # Сравниваем текст выбранного товара и товара в корзине
    sale_page.compare_element_texts(
        sale_page.text_of_the_selected_product,
        sale_page.text_of_the_product_in_the_basket
    )


@allure.feature('Checking if the cart is empty')
@allure.story('Checking the basket')
@allure.title('Проверка пустой корзины')
@allure.description('Этот тест проверяет отображение соответствующего текста в пустой корзине')
@pytest.mark.regression
def test_checking_if_the_cart_is_empty(sale_page):

    # Открытие страницы в браузере
    sale_page.open_page()

    # Открытие корзины
    sale_page.opening_empty_basket()

    # Проверка соответствующего текста в пустой корзине
    sale_page.check_text_after_creating_an_account(
        sale_page.element_text_empty_basket,
        sale_page.text_to_check_the_empty_basket
    )


@allure.feature('Open link pants in new tab')
@allure.story('Open link')
@allure.title('Открытие ссылки Pants в новой вкладке')
@allure.description(
    'Этот тест проверяет открытие ссылки Pants в новой вкладке, переход на новую вкладку и проверку текста'
)
@pytest.mark.regression
def test_open_link_pants(sale_page):

    # Открытие страницы в браузере
    sale_page.open_page()

    # Открытие ссылки в новой вкладке
    sale_page.open_link_pants_new_tab()

    # Проверка соответствующего текста на новой вкладке
    sale_page.compare_element_texts(
        sale_page.element_text_pants_new_tab,
        sale_page.element_link_text_pants
    )
