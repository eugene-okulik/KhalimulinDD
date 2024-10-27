import allure
from playwright.sync_api import Page, expect, BrowserContext
from test_UI_khalimulindd_pw.pages.base_page import BasePage
from test_UI_khalimulindd_pw.pages.locators import sale_page_locators as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def __init__(self, page: Page, context: BrowserContext, timeout: int = 90000):
        super().__init__(page, context, timeout)  # Наследование от родительского класса
        self.text_link_pants_tab = None
        self.link_pants = None

    @allure.step('Adding an item to the cart and opening the cart')
    def adding_sixth_product_to_cart(self):
        self.find(loc.button_shop_women_deals_loc).click()

        element_sixth_product = self.find(loc.sixth_product_loc)
        element_sixth_product_size = self.find(loc.sixth_product_size_loc)
        element_sixth_product_color = self.find(loc.sixth_product_color_loc)
        element_sixth_product_button = self.find(loc.sixth_product_button_loc)

        element_sixth_product.hover()
        element_sixth_product_size.click()
        element_sixth_product_color.click()
        element_sixth_product_button.click()

        expect(self.page.locator(loc.basket_loc).nth(0)).not_to_have_attribute("class", "loading", timeout=10000)
        self.find(loc.button_basket_loc).click()

    # Свойство для получения элемента выбранного товара
    @property
    def text_of_the_selected_product(self):
        return self.find(loc.sixth_product_loc)

    # Свойство для получения элемента товара в корзине
    @property
    def text_of_the_product_in_the_basket(self):
        return self.find(loc.text_product_in_basket_loc)

    @allure.step('Opening an empty basket')
    def opening_empty_basket(self):
        self.find(loc.button_empty_basket_loc).click()

    # Свойство для получения элемента текста пустой корзины
    @property
    def element_text_empty_basket(self):
        return self.find(loc.empty_basket_text_loc)

    # Свойство для передачи текста, который отображается при открытии пустой корзины
    @property
    def text_to_check_the_empty_basket(self):
        return 'You have no items in your shopping cart.'

    @allure.step('Opening the Pants link in a new tab and checking the text')
    def open_link_pants_new_tab(self):
        self.link_pants = self.page.get_by_role("link", name="Pants").nth(1)
        self.link_pants.click(modifiers=["Control"])
        self.text_link_pants_tab = self.wait_for_new_page_and_get_element(locator=loc.pants_text_new_tab_loc)

    # Свойство для получения элемента текста Pants в новом окне
    @property
    def element_text_pants_new_tab(self):
        return self.text_link_pants_tab

    # Свойство для передачи текста нажатой ссылки Pants
    @property
    def element_link_text_pants(self):
        return self.link_pants
