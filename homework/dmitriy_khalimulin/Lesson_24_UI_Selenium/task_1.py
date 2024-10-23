import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_add_to_cart(driver):
    driver.get('https://www.demoblaze.com/index.html')

    # Находим первый товар с помощью явного ожидания
    wait = WebDriverWait(driver, 10)
    product = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@class="card-title"]/child::a')))
    product_text = product.text

    # Открываем товар в новой вкладке
    ActionChains(driver).key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()

    # Переключаемся на новую вкладку
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Находим кнопку Add to cart и нажимаем
    wait = WebDriverWait(driver, 10)
    add_to_card = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@onclick="addToCart(1)"]')))
    add_to_card.click()

    # Явное ожидание для появления alert
    WebDriverWait(driver, 4).until(EC.alert_is_present())

    # Подтверждаем добавление в Allert
    alert = Alert(driver)
    alert.accept()

    # Закрытие новой вкладки и переключение фокуса на предыдущую
    driver.close()
    driver.switch_to.window(tabs[0])

    # Переход в корзину
    driver.find_element(By.ID, 'cartur').click()

    # Поиск добавленного товара
    text_in_card = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="tbodyid"]/descendant::td[2]'))).text

    # Проверка добавленного товара
    assert product_text == text_in_card


def test_mouse_hover(driver):
    driver.implicitly_wait(3)
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')

    # Поиск первого товара
    first_product = driver.find_element(
        By.XPATH, '//ol[@class="products list items product-items"]/descendant::div[1]/descendant::strong'
    )
    text_first_product = first_product.text

    # Поиск кнопки Add to Compare
    button_add_to_compair = driver.find_element(
        By.XPATH, '//div[@class="product-item-inner"]/descendant::div[3]/child::a[2]'
    )

    # Наведение курсора на товар и нажатие кнопки Add to Compare
    ActionChains(driver).move_to_element(first_product).click(button_add_to_compair).perform()

    # Поиск добавленного товара
    assert_compare = driver.find_element(By.LINK_TEXT, 'Push It Messenger Bag')
    text_in_assert_compare = assert_compare.text

    # Прокрутка до области с помощью JavaScript
    driver.execute_script("arguments[0].scrollIntoView();", assert_compare)

    # Проверка добавленного товара
    assert text_first_product == text_in_assert_compare
