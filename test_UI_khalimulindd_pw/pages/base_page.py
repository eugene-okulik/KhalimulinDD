import allure
from playwright.sync_api import Page, expect, BrowserContext, Locator


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page, context: BrowserContext, timeout: int = 90000):
        """Инициализация драйвера и ActionChains"""
        self.page = page
        self.context = context
        self.timeout = timeout

    @allure.step('Open the page')
    def open_page(self):
        """Метод для открытия страницы"""
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}', timeout=self.timeout)
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    @allure.step('Find element by locator')
    def find(self, locator) -> Locator:
        """Метод поиска элемента по локатору"""
        return self.page.locator(locator)

    @staticmethod
    @allure.step('Comparing the text of two elements')
    def compare_element_texts(element_1: Locator, element_2: Locator):
        """Сравнение текста двух уже найденных элементов или строк"""

        # Ожидание появления текста в элементе
        expect(element_2).to_be_visible(timeout=5000)

        # Присваивание переменной текст локатора
        element_2_text = element_2.inner_text()

        # Проверка соответствия текстов
        expect(element_1).to_have_text(element_2_text)

    @allure.step('Checking the text of the found element')
    def check_text_after_creating_an_account(self, locator: Locator, expected_text: str):
        """Метод для проверки текста найденного элемента на странице"""

        # Ожидание видимости первого элемента
        expect(locator.first).to_be_visible(timeout=5000)

        # Проверка текста элемента на соответствие ожидаемому тексту
        expect(locator.first).to_have_text(expected_text)

    @staticmethod
    @allure.step('Checking the sorting of products in ascending order')
    def check_prices_sorted_ascending(price_locator):
        """Метод для проверки, что цены товаров отсортированы по возрастанию"""

        prices = []
        count = price_locator.count()
        for i in range(count):
            price_text = price_locator.nth(i).inner_text().replace('$', '').replace(',', '').strip()
            prices.append(float(price_text))

        # Обычный assert вместо expect для проверки сортировки списка
        assert prices == sorted(prices), f"Prices are not sorted: {prices}"

    @allure.step('Open and go to a new tab and return an element')
    def wait_for_new_page_and_get_element(self, locator: str):
        """Ожидает открытия новой страницы и возвращает элемент по локатору."""
        with self.context.expect_page() as new_page_event:
            new_page = new_page_event.value

        # Переключение на новую вкладку
        new_page.bring_to_front()

        # Ожидание загрузки новой страницы
        new_page.wait_for_load_state("load", timeout=self.timeout)

        # Поиск элемента по локатору (строка)
        result = new_page.locator(locator)

        # Ожидание появления элемента
        expect(result).to_be_visible(timeout=5000)

        return result
