from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_text_check(driver):
    driver.get('https://www.demoblaze.com/index.html')

    # Находим первый товар с помощью явного ожидания
    wait = WebDriverWait(driver, 2)
    product = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@class="card h-100"]/child::a')))

    # Открываем товар в новой вкладке
    ActionChains(driver).key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()

    # Переключаемся на новую вкладку
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Находим кнопку Add to cart и нажимаем
    wait = WebDriverWait(driver, 2)
    add_to_card = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@onclick="addToCart(1)"]')))
    add_to_card.click()

    # Явное ожидание до 2 секунд появления alert
    WebDriverWait(driver, 2).until(EC.alert_is_present())

    # Подтверждаем добавление в Allert
    alert = Alert(driver)
    alert.accept()
