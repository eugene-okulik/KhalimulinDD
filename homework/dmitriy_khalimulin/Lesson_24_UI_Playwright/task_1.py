from playwright.sync_api import Page


def test_enter_login_and_password(page: Page):
    page.goto('https://the-internet.herokuapp.com/')

    # Поиск и нажатие ссылки Form Authentication
    page.get_by_role('link', name="Form Authentication").click()

    # Поиск и ввода данных для входа
    page.get_by_role('textbox', name="username").fill('Katalov')
    page.get_by_role('textbox', name="password").fill('Katalov123!')

    # Нажатие кнопки Login
    page.get_by_role('button', name=" Login").click()
