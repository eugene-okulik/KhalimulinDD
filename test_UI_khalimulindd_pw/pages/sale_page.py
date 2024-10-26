import allure
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from pages.locators import sale_page_locators as loc
from selenium.webdriver.remote.webdriver import WebDriver


class SalePage(BasePage):
    page_url = '/sale.html'

    def __init__(self, driver: WebDriver, timeout: int = 10):
        super().__init__(driver, timeout)  # Наследование от родительского класса
        self.text_link_pants = None

    @allure.step('Adding an item to the cart and opening the cart')
    def adding_sixth_product_to_cart(self):
        self.find(loc.button_shop_women_deals_loc).click()

        self.scroll(loc.sixth_product_loc)

        element_sixth_product = self.find(loc.sixth_product_loc)
        element_sixth_product_size = self.find(loc.sixth_product_size_loc)
        element_sixth_product_color = self.find(loc.sixth_product_color_loc)
        element_sixth_product_button = self.find(loc.sixth_product_button_loc)

        self.actions.move_to_element(element_sixth_product)
        self.actions.click(element_sixth_product_size)
        self.actions.click(element_sixth_product_color)
        self.actions.click(element_sixth_product_button)
        self.actions.perform()

        self.scroll(loc.basket_loc)

        self.wait_for_element_not_to_have_text_in_attribute(locator=loc.basket_loc, attribute='class', text='loading')
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
        link_pants = self.find(loc.pants_link_loc)
        self.text_link_pants = self.text_extraction(loc.pants_link_loc)
        self.actions.key_down(Keys.CONTROL).click(link_pants).key_up(Keys.CONTROL).perform()
        self.switch_to_new_tab()

    # Свойство для передачи текста нажатой ссылки Pants
    @property
    def element_link_text_pants(self):
        return self.text_link_pants

    # Свойство для получения элемента текста Pants в новом окне
    @property
    def element_text_pants_new_tab(self):
        return self.find(loc.pants_text_new_tab_loc)
