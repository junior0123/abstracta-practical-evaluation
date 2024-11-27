import os
import pytest
from pytest_bdd import when, then, scenarios, parsers
from .common_steps import *
from dotenv import load_dotenv
from ..pages.home_page import HomePage
from ..pages.components.top_bar_component import TopBarComponent
scenarios(os.path.join(os.path.dirname(__file__), '../scenarios/scrape_products.feature'))
load_dotenv()
BASE_URL = os.getenv('BASE_URL')
USERNAME = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

@pytest.fixture(scope="function")
def top_bar_component(page):
    return TopBarComponent(page)

@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)

@then("the user saves the product information to a text file")
def save_data(top_bar_component):
    top_bar_component.click_on_logout_button()

@when(parsers.parse('the user navigates to and scrapes product information from the first "{num_pages}" pages'))
def step_when(home_page, num_pages):
    home_page.navigate_through_product_pages(int(num_pages))
