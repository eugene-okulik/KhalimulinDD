from playwright.sync_api import Page


def test_css_style(page: Page):

    # Выполняем переход на сайт и сразу начинаем выполнение теста
    page.goto('https://demoqa.com/dynamic-properties', wait_until='domcontentloaded')

    # Ждем, пока у кнопки появится класс .text-danger и кликаем ее
    page.wait_for_selector('#colorChange.text-danger').click()
