from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(6)
    chrome_driver.maximize_window()
    yield chrome_driver


def test_single_select(driver):

    driver.get('https://www.qa-practice.com/elements/select/single_select')

    # Поиск и нажатие и выбор DropDown в поле Choose language
    select = driver.find_element(By.ID, 'id_choose_language')
    dropdown = Select(select)
    dropdown.select_by_value('3')

    # Получение текста выбранной опции
    selected_option_text = dropdown.first_selected_option.text

    # Поиск и нажатие кнопки Submit
    button = driver.find_element(By.ID, 'submit-id-submit')
    button.click()

    # Поиск и проверка выбранного елемента DropDown
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == selected_option_text
    print(result_text.text)


def test_click_start(driver):

    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    text_hello = 'Hello World!'

    # Поиск и нажатие на кнопку Start
    button_start = driver.find_element(By.XPATH, '//*[@id="start"]/child::button')
    button_start.click()

    # Проверка отображения теста "Hello World!"
    result_is_text = driver.find_element(By.XPATH, '//*[@id="finish"]/child::h4')
    assert result_is_text.text == text_hello
