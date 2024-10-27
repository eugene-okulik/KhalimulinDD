import pytest
from test_UI_khalimulindd_pw.pages.sale_page import SalePage
from test_UI_khalimulindd_pw.pages.create_account_page import CreateAccount
from test_UI_khalimulindd_pw.pages.collections_eco_friendly_page import CollectionsEcoFriendly


@pytest.fixture()
def create_account_page(page, context):
    return CreateAccount(page, context)


@pytest.fixture()
def collections_eco_friendly_page(page, context):
    return CollectionsEcoFriendly(page, context)


@pytest.fixture()
def sale_page(page, context):
    return SalePage(page, context)
