import allure
from playwright.sync_api import Page, expect, BrowserContext
from test_UI_khalimulindd_pw.pages.base_page import BasePage
from test_UI_khalimulindd_pw.pages.locators import collections_eco_friendly_locators as loc


class CollectionsEcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def __init__(self, page: Page, context: BrowserContext, timeout: int = 90000):
        super().__init__(page, context, timeout)  # Наследование от родительского класса
        self.text_button_shorts_text = None

    @allure.step('Adding the first product for comparison')
    def add_to_first_compare(self):
        first_element = self.find(loc.first_element_loc)
        button_add_to_compare = self.find(loc.button_add_to_compair_loc)
        first_element.hover()
        expect(button_add_to_compare).to_be_enabled(timeout=5000)
        button_add_to_compare.click()

    # Свойство для получения элемента первого товара
    @property
    def first_product(self):
        return self.find(loc.first_element_loc)

    # Свойство для получения элемента товара в сравнении
    @property
    def product_in_comparison(self):
        return self.find(loc.compare_product_loc)

    @allure.step('Go to the Shorts subtab in the Men tab')
    def click_the_button_and_search_for_the_element_shorts(self):
        element_men = self.find(loc.men_loc)
        element_men_bottoms = self.find(loc.men_bottoms_loc)
        element_men_bottoms_shorts = self.find(loc.men_bottoms_shorts_loc)

        self.text_button_shorts_text = self.find(loc.men_bottoms_shorts_loc)

        element_men.hover()
        element_men_bottoms.hover()
        element_men_bottoms_shorts.click()

    # Свойство для передачи текста нажатой кнопки
    @property
    def text_button_shorts(self):
        return self.text_button_shorts_text

    # Свойство для получения элемента Shorts на новой открытой странице
    @property
    def text_shorts_is_open_page(self):
        return self.find(loc.text_shorts_loc)

    @allure.step('Search and click to sort in ascending order')
    def sort_by_price(self):
        self.find(loc.sort_by_loc).select_option('Price')

        # Ожидаем, пока элементы с ценами появятся после сортировки
        self.page.wait_for_selector(loc.sorted_goods_price_loc, state='visible')

    # Свойство для получения всех цен на странице
    @property
    def text_price(self):
        return self.page.locator(loc.sorted_goods_price_loc)
