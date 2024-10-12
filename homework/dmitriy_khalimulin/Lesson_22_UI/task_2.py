from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_filling_out_the_questionnaire(driver):

    first_name = 'Dmitriy'
    last_name = 'Konovalov'
    email = 'Konovalov@mail.ru'
    phone_number = '89029384746'
    subjects = 'Hist'
    current_address = 'Nosova 95'

    driver.get('https://demoqa.com/automation-practice-form')

    # Поиск и подстановка значения в поле First Name
    field_first_name = driver.find_element(By.ID, 'firstName')
    field_first_name.send_keys(first_name)

    # Поиск и подстановка значения в поле Last Name
    field_last_name = driver.find_element(By.ID, 'lastName')
    field_last_name.send_keys(last_name)

    # Поиск и подстановка значения в поле Email
    field_email = driver.find_element(By.ID, 'userEmail')
    field_email.send_keys(email)

    # Нажатие на Radio Button для указания Gender
    radio_button_gender = driver.find_element(By.CSS_SELECTOR, '[for ="gender-radio-1"]')
    radio_button_gender.click()

    # Поиск и подстановка значения в поле Mobile
    field_phone_number = driver.find_element(By.ID, 'userNumber')
    field_phone_number.send_keys(phone_number)

    # Поиск и указание даты в DatePicker в поле Date of Birth
    field_date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    field_date_of_birth.click()
    choice_of_number = driver.find_element(By.CLASS_NAME, 'react-datepicker__day--010')
    choice_of_number.click()

    # Поиск и подстановка значения в поле Subjects
    field_subjects = driver.find_element(By.ID, 'subjectsInput')
    field_subjects.send_keys(subjects)
    wait = WebDriverWait(driver, 3)

    dropdown_item = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".subjects-auto-complete__menu-list div[id*='react-select']")))

    dropdown_item.click()

    # Выбор Check Box для указания Hobbies
    check_box_hobbies = driver.find_element(By.CSS_SELECTOR, '[for ="hobbies-checkbox-1"]')
    check_box_hobbies.click()

    # Поиск и подстановка значения в поле Current Address
    field_current_address = driver.find_element(By.ID, 'currentAddress')
    field_current_address.send_keys(current_address)

    # Выбор State из Dropdown
    dropdown_search_state = driver.find_element(By.XPATH, '//*[@id="state"]/child::div')

    # Прокрутка до кнопки с помощью JavaScript
    driver.execute_script("arguments[0].scrollIntoView();", dropdown_search_state)
    dropdown_search_state.click()

    dropdown_state = wait.until(
        EC.element_to_be_clickable((By.ID, "react-select-3-option-0")))

    dropdown_state.click()

    # Выбор City из Dropdown
    dropdown_search_city = driver.find_element(By.XPATH, '//*[@id="city"]/child::div')
    dropdown_search_city.click()

    dropdown_city = wait.until(
        EC.element_to_be_clickable((By.ID, "react-select-4-option-1")))

    dropdown_city.click()

    # Нажатие кнопки Submit
    submit = driver.find_element(By.ID, 'submit')
    submit.click()

    # Распечатка данных из таблицы
    form_data = {}

    date = driver.find_elements(By.XPATH, '//*[@class="table-responsive"]/descendant::tbody/child::tr')

    for tr in date:
        cells = tr.find_elements(By.TAG_NAME, 'td')

        if len(cells) == 2:  # Убедимся, что в строке две ячейки
            key = cells[0].text  # Первая ячейка - это ключ
            value = cells[1].text  # Вторая ячейка - это значение

            # Добавляем ключ-значение в словарь
            form_data[key] = value

    # Вывод полученного словаря
    print(form_data)
