from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_in_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def shold_be_right_product_name_in_message(self):
        product_name = self.browser.find_element\
        (*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element\
        (*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message, "Wrong product in message"

    def shold_be_right_product_price_in_message(self):
        product_price = self.browser.find_element\
        (*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_message = self.browser.find_element\
        (*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text
        assert product_price == product_price_in_message, "Wrong price in message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
