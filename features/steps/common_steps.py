import os
import pytest
from pytest_bdd import given, when
from dotenv import load_dotenv
from ..pages.login_page import LoginPage
from ..pages.components.top_bar_component import TopBarComponent

load_dotenv()
BASE_URL = os.getenv('BASE_URL')
USERNAME = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)

@pytest.fixture(scope="function")
def top_bar_component(page):
    return TopBarComponent(page)
@given('the user is on the homepage')
def step_given(login_page):
    login_page.navigate(BASE_URL)
    
@given("the user is logged in with valid credentials")
def user_logged_in(login_page, top_bar_component):
    top_bar_component.click_on_login_button()
    login_page.login(USERNAME,PASSWORD)
    
@when('the user logs out')
def step_when(top_bar_component):
    top_bar_component.click_on_logout_button()