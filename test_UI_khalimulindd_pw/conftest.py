import pytest
from pages.sale_page import SalePage
from pages.create_account_page import CreateAccount
from pages.collections_eco_friendly_page import CollectionsEcoFriendly


@pytest.fixture()
def create_account_page(page, context):
    return CreateAccount(page, context)


@pytest.fixture()
def collections_eco_friendly_page(page, context):
    return CollectionsEcoFriendly(page, context)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


# @pytest.fixture()
# def driver():
#     """Фикстура для открытия браузера  с опциями"""
#     options.add_argument('start-maximized')
#     # options.add_experimental_option('detach', True)
#     chrome_driver = webdriver.Chrome(options=options)
#     return chrome_driver
