from playwright.sync_api import Page


def test_filling_out_the_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form', wait_until='domcontentloaded')

    # Поиск и ввод данных в поле First Name
    page.get_by_placeholder('First Name').fill('Ivan')

    # Поиск и ввод данных в поле Last Name
    page.get_by_placeholder('Last Name').fill('Katalov')

    # Поиск и ввод данных в поле Email
    page.get_by_placeholder('name@example.com').fill('katalov_ivan@mail.ru')

    # Поиск и нажатие на checkbox в области Gender
    page.locator('[for ="gender-radio-1"]').check()

    # Поиск и ввод данных в поле Mobile Number
    page.get_by_placeholder('Mobile Number').fill('89029384746')

    # Поиск и нажатие на поле Date of Birth
    page.locator('#dateOfBirthInput').click()

    # Поиск и нажатие на число 31 в date picker
    page.locator('//*[@class="react-datepicker__day react-datepicker__day--031"]').click()

    # Поиск и ввод данных в поле Subjects и выбор значения в выпадающем списке
    page.locator('#subjectsInput').fill('Eng')
    page.locator('#react-select-2-option-0').click()

    # Поиск и нажатие на checkbox в области Hobbies
    page.locator('[for ="hobbies-checkbox-1"]').check()

    # Поиск и ввод данных в поле Current Address
    page.get_by_placeholder('Current Address').fill('Testoviy comment')

    # Поиск и выбор значения в выпадающем списке в поле State
    page.locator('//*[@id="state"]/child::div').click()
    page.locator('#react-select-3-option-0').click()

    # Поиск и выбор значения в выпадающем списке в поле City
    page.locator('//*[@id="city"]/child::div').click()
    page.locator('#react-select-4-option-1')

    # Поиск и нажатие кнопки Submit
    page.locator('#submit').click()
