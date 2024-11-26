
# from features.steps.common_steps import *
# from features.steps.scrape_steps import *

import pytest


@pytest.fixture(scope="function")
def context(browser):

    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        user_agent="custom-agent"
    )
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
