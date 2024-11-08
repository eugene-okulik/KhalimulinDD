from playwright.sync_api import Page, expect


def test_alert_text(page: Page):
    text_is_you_selected = 'Ok'

    # Ожидаем в тесте появление allert и жмем Ok
    page.on('dialog', lambda alert: alert.accept())

    # Выполняем переход на сайт
    page.goto('https://www.qa-practice.com/elements/alert/confirm')

    # Поиск и нажатие на кнопку Click
    page.get_by_role('link', name='Click').click()

    # Поиск текста в области You selected
    result_text = page.locator('#result-text')

    # Проверка отображаемого текста
    expect(result_text).to_have_text(text_is_you_selected)
