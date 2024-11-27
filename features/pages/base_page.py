from playwright.sync_api import Page
from utils.logger_config import setup_logger
logger = setup_logger()

class BasePage:
    """
    This is a base page class for handling common browser interactions using Playwright.

    Attributes:
        page (Page): Playwright Page object that represents a browser page.

    Methods:
        __init__(self, page: Page): Initializes the BasePage with a Playwright page.
        navigate(self, url: str): Navigates to the provided URL.
        click(self, locator: str): Clicks on the element matching the provided locator.
        fill_text(self, locator: str, text: str): Fills the provided text in the input element located by the locator.
    """

    def __init__(self, page: Page):
        """
        Initializes the BasePage with a Playwright page.

        Args:
            page (Page): The Playwright Page object that represents the browser page.
        """
        self.page = page
        logger.info(f"BasePage initialized with page: {page.url}")

    def navigate(self, url: str):
        """
        Navigates to the specified URL in the browser.

        Args:
            url (str): The URL to navigate to.
        """
        logger.info(f"Navigating to URL: {url}")
        self.page.goto(url)
        logger.info(f"Successfully navigated to: {url}")

    def click(self, locator: str):
        """
        Clicks on the element located by the provided locator.

        Args:
            locator (str): The locator of the element to click.
        """
        logger.info(f"Attempting to click on element with locator: {locator}")
        self.page.click(locator)
        logger.info(f"Successfully clicked on element with locator: {locator}")

    def fill_text(self, locator: str, text: str):
        """
        Fills the provided text in the input element located by the locator.

        Args:
            locator (str): The locator of the input element.
            text (str): The text to fill in the input element.
        """
        logger.info(f"Filling text '{text}' into element with locator: {locator}")
        self.page.fill(locator, text)
        logger.info(f"Successfully filled text into element with locator: {locator}")
