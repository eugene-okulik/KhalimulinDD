import allure
from playwright.sync_api import Page, expect, BrowserContext, Locator


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page, context: BrowserContext, timeout: int = 10):
        """Инициализация драйвера и ActionChains"""
        self.page = page
        self.context = context
        self.timeout = timeout

    @allure.step('Open the page')
    def open_page(self):
        """Метод для открытия страницы"""
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}', timeout=90000)
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    @allure.step('Find element by locator')
    def find(self, locator) -> Locator:
        """Метод поиска элемента по локатору"""
        return self.page.locator(locator)

    # @allure.step('Extracting found text from the locator')
    # def text_extraction(self, locator):
    #     """Метод для извлечения текста из элемента, найденного по локатору"""
    #     element = self.find(locator)
    #     return element

    @staticmethod
    @allure.step('Comparing the text of two elements')
    def compare_element_texts(element_1: Locator, element_2: Locator):
        """Сравнение текста двух уже найденных элементов или строк"""

        # Ожидание появления текста в элементе
        expect(element_2).to_be_visible(timeout=5000)

        element_2_text = element_2.text_content() or element_2.inner_text()

        print(f'Первый элемент {element_1.inner_text()}')
        print(f'Второй элемент {element_2_text}')
        print(f'Входной второй {element_2}')

        # Сравнение текстов с использованием expect
        expect(element_1).to_have_text(element_2_text)

    # @allure.step('Waiting for element to appear')
    # def wait_for_element(self, locator: tuple[str, str], condition: EC):
    #     """Метод явного ожидания элемента"""
    #     return self.wait.until(condition(locator))

    @allure.step('Wait until an element attribute contains text')
    def wait_for_element_not_to_have_text_in_attribute(self, locator, attribute: str, text: str):
        """Метод ожидания, пока атрибут элемента не будет содержать текст"""

        # Локатор элемента
        element = locator

        # Ожидание, пока атрибут не перестанет содержать указанный текст
        while text in element.get_attribute(attribute):
            # Обновляем атрибут, чтобы проверить его состояние
            if text not in element.get_attribute(attribute):
                break
            element.wait_for(timeout=100)  # Устанавливаем интервал ожидания

        # Проверка, что атрибут больше не содержит текст
        expect(element.get_attribute(attribute)).not_to_contain(text)

    @allure.step('Checking the text of the found element')
    def check_text_after_creating_an_account(self, locator: Locator, expected_text: str):
        """Метод для проверки текста найденного элемента на странице"""

        # Ожидание видимости первого элемента
        expect(locator.first).to_be_visible(timeout=5000)

        # Проверка текста элемента на соответствие ожидаемому тексту
        expect(locator.first).to_have_text(expected_text)

    # @allure.step('Selecting an item from a drop-down list')
    # def select_by_value(self, select_locator: tuple, value_locator: tuple):
    #     """Метод для выбора элемента из выпадающего списка с использованием локаторов"""
    #
    #     # Находим элемент select по локатору (кортежу)
    #     select_element = self.find(select_locator)
    #
    #     # Инициализируем объект Select
    #     dropdown = Select(select_element)
    #
    #     # Находим элемент, который нужно выбрать по переданному локатору для значения
    #     value_element = self.find(value_locator)
    #
    #     # Получаем значение атрибута 'value' элемента
    #     value = value_element.get_attribute("value")
    #
    #     # Выбираем элемент в select по значению
    #     dropdown.select_by_value(value)

    @staticmethod
    @allure.step('Checking the sorting of products in ascending order')
    def check_prices_sorted_ascending(price_locator):
        """Метод для проверки, что цены товаров отсортированы по возрастанию"""

        prices = []
        count = price_locator.count()
        for i in range(count):
            price_text = price_locator.nth(i).inner_text().replace('$', '').replace(',', '').strip()
            prices.append(float(price_text))

        print(f'Список цен: {prices}')

        # Обычный assert вместо expect для проверки сортировки списка
        assert prices == sorted(prices), f"Prices are not sorted: {prices}"

    @allure.step('Switch to a new tab')
    def switch_to_new_tab(self):
        """Метод для переключения на новую вкладку"""

        # Ожидание появления новой страницы (вкладки)
        pages = self.context.pages
        if len(pages) < 2:
            self.context.wait_for_event("page")

        # Переключаемся на последнюю (новую) вкладку
        new_tab = self.context.pages[-1]
        new_tab.bring_to_front()  # Переключаемся на новую вкладку
