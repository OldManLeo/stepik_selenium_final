from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket page items presented"

    def should_be_empty_basket_message(self):
        basket_value = self.browser.find_element \
            (*BasketPageLocators.BASKET_ITEMS_EMPTY_MESSAGE).text
        assert "Your basket is empty." in basket_value , "No empty basket message"
