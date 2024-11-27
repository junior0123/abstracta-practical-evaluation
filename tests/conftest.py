
import pytest

@pytest.fixture(scope="function")
def context(browser):

    context = browser.new_context(
        user_agent="custom-agent",
        noViewport = True,
    )
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
