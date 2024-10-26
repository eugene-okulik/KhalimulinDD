from selenium.webdriver.common.by import By

button_shop_women_deals_loc = (By.XPATH, '//*[@class="more button"]')
sixth_product_loc = (
    By.XPATH, '//*[@class="item product product-item"][6]'
              '/descendant::div[@class="product details product-item-details"]'
              '/descendant::a[1]'
)
sixth_product_size_loc = (
    By.XPATH, '//*[@class="item product product-item"][6]/descendant::div[@id="option-label-size-143-item-167"]'
)
sixth_product_color_loc = (
    By.XPATH, '//*[@class="item product product-item"][6]/descendant::div[@id="option-label-color-93-item-56"]'
)
sixth_product_button_loc = (
    By.XPATH, '//*[@class="item product product-item"][6]'
              '/descendant::div[@class="product-item-inner"]'
              '/descendant::button'
)
basket_loc = (By.CSS_SELECTOR, '.counter.qty')
button_basket_loc = (By.CSS_SELECTOR, '.counter-number')
text_product_in_basket_loc = (By.XPATH, '//*[@class="product-item-details"]/descendant::a[1]')
button_empty_basket_loc = (By.CSS_SELECTOR, '.action.showcart')
empty_basket_text_loc = (By.XPATH, '//*[@class="subtitle empty"]')
pants_link_loc = (By.LINK_TEXT, 'Pants')
pants_text_new_tab_loc = (By.XPATH, '//*[@id="page-title-heading"]/child::span')
