from playwright.sync_api import Page, expect, BrowserContext


def test_tabs(page: Page, context: BrowserContext):
    text_in_new_tab = 'I am a new page in a new tab'

    # Выполняем переход на сайт
    page.goto('https://www.qa-practice.com/elements/new_tab/button')

    # Поиск затем нажатие на кнопку Click
    button_click = page.get_by_role('link', name='Click')
    button_click.click()

    # Фиксируем новую открытую вкладку
    with context.expect_page() as new_page_event:
        new_page = new_page_event.value

        # Поиск элемента с текстом
        result = new_page.locator('#result-text')

        # Проверка совпадения отображаемого текста
        expect(result).to_have_text(text_in_new_tab)

        # Проверка что кнопка на основной странице enabled
        expect(button_click).to_be_enabled()
