import os
import pytest
from .common_steps import *
from pytest_bdd import given, when, then, scenarios, parsers
from dotenv import load_dotenv
from ..pages.login_page import LoginPage
from ..pages.home_page import HomePage
from ..pages.product_page import ProductPage
from ..pages.cart_page import CartPage
from ..pages.components.top_bar_component import TopBarComponent
scenarios(os.path.join(os.path.dirname(__file__), '../scenarios/purchase.feature'))
load_dotenv()
BASE_URL = os.getenv('BASE_URL')
NAME = os.getenv('NAME')
COUNTRY = os.getenv('COUNTRY')
CITY = os.getenv('CITY')
CREDIT_CARD_NUMBER = os.getenv('CREDIT_CARD_NUMBER')
MONTH = os.getenv('MONTH')
YEAR = os.getenv('YEAR')

@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)

@pytest.fixture(scope="function")
def top_bar_component(page):
    return TopBarComponent(page)

@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)

@pytest.fixture(scope="function")
def product_page(page):
    return ProductPage(page)

@pytest.fixture(scope="function")
def cart_page(page):
    return CartPage(page)

@when(parsers.parse('the user selects the product "{product_name}" from the product listing'))
def step_when(home_page, product_name):
    home_page.click_on_select_item(product_name)

@when('the user adds the product to the cart')
def step_when(product_page):
    product_page.click_on_add_to_cart_button()
    

@when('the user navigates to the Cart section')
def step_when(top_bar_component):
    top_bar_component.click_on_cart_button()

@when('the user enters valid test data for the purchase')
def step_when(cart_page):
    cart_page.fill_order_information(NAME, COUNTRY, CITY, CREDIT_CARD_NUMBER, MONTH, YEAR)
    cart_page.click_on_purchase_order_button()
    
@when('the user proceeds to the checkout')
def step_when(cart_page):
    cart_page.click_on_place_order_button()
@then('the user should see a confirmation message with the order details')
def step_then(cart_page, top_bar_component):
    cart_page.verify_order_information()
    cart_page.click_on_confirmation_order_button()
    top_bar_component.click_on_logout_button()

@then(parsers.parse('the product "{item_name}" should still be in the cart'))
def step_then(cart_page, item_name, top_bar_component):
    cart_page.verify_exist_item(item_name)
    cart_page.delete_selected_item_from_cart(item_name)
    top_bar_component.click_on_logout_button()
    
@when('the user logs in again with valid credentials')
def step_when(login_page, top_bar_component):
    top_bar_component.click_on_login_button()
    login_page.login(USERNAME,PASSWORD)
    
@when('the user goes back to the product listing')
def step_when(top_bar_component):
    top_bar_component.click_on_home_button()

@when(parsers.parse('the user removes the product "{item_name}" from the cart'))
def step_when(cart_page, item_name):
    cart_page.delete_selected_item_from_cart(item_name)


@then(parsers.parse('the cart should no longer contain the "{item_name}" product'))
def step_when(cart_page, item_name):
    cart_page.verify_item_not_exist(item_name)


@then(parsers.parse('the cart should only contain the "{item_name}" product'))
def step_then(cart_page, item_name):
    cart_page.verify_quantity_of_products_in_the_cart()
    cart_page.verify_exist_item(item_name)
    cart_page.delete_selected_item_from_cart(item_name)
    
