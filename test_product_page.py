from .pages.product_page import ProductPage
from .pages.locators import LoginPageLocators
import pytest
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.shold_be_right_product_name_in_message()
    page.shold_be_right_product_price_in_message()


@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6",  pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.shold_be_right_product_name_in_message()
    page.shold_be_right_product_price_in_message()
    time.sleep(120)
