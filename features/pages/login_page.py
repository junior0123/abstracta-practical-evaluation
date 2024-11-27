from .base_page import BasePage
from playwright.sync_api import expect
from utils.logger_config import setup_logger

# Setting up the logger
logger = setup_logger()

class LoginPage(BasePage):
    """This class represents the login page and provides methods for logging in, canceling login, and navigating to the login page."""

    USERNAME_FIELD = "#loginusername"
    PASSWORD_FIELD = "#loginpassword"
    LOGIN_BUTTON = 'button[onclick="logIn()"]'

    def login(self, username: str, password: str):
        """
        Fills the login form with the provided username and password, and clicks the login button.
        
        Args:
            username (str): The username to log in with.
            password (str): The password associated with the username.
        """
        logger.info(f"Attempting to log in with username: {username}")
        self.fill_text(self.USERNAME_FIELD, username)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        logger.info("Login button clicked")

    def click_on_cancel_button(self):
        """Clicks the cancel (close) button to exit the login form."""
        logger.info("Clicking on cancel button to close the login form.")
        self.page.get_by_label("Log in").get_by_text("Close").click()

    def navigate(self, url: str):
        """
        Navigates to the login page URL and waits for the login page to load.
        
        Args:
            url (str): The URL of the login page.
        """
        logger.info(f"Navigating to URL: {url}")
        super().navigate(url)
        expect(self.page.locator("#tbodyid")).to_be_visible()
      
