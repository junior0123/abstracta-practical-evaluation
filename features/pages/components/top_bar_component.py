from ..base_page import BasePage
from utils.logger_config import setup_logger

# Setting up the logger
logger = setup_logger()

class TopBarComponent(BasePage):
    """This class represents the top bar component of the website, providing methods for interacting with various elements in the top bar."""

    NAME_USER = "#nameofuser"
    HOME_LINK = ".nav-link[href='index.html']"
    CART_LINK = '#cartur'
    LOGIN_LINK = '#login2'
    LOGOUT_LINK = '#logout2'

    def click_on_cart_button(self):
        """
        Clicks on the 'Cart' link in the top bar to navigate to the shopping cart page.
        Logs the action to track the navigation event.
        """
        logger.info("Clicking on the 'Cart' button in the top bar.")
        self.click(self.CART_LINK)
        logger.info("Navigated to the 'Cart' page.")

    def click_on_login_button(self):
        """
        Clicks on the 'Login' link in the top bar to open the login modal.
        Waits for the modal to be visible and logs the action.
        """
        logger.info("Clicking on the 'Login' button in the top bar.")
        self.click(self.LOGIN_LINK)
        self.page.wait_for_selector("#logInModalLabel")
        logger.info("Login modal is now visible.")

    def click_on_logout_button(self):
        """
        Clicks on the 'Logout' link in the top bar to log out the user.
        Logs the action to track the logout event.
        """
        logger.info("Clicking on the 'Logout' button in the top bar.")
        self.click(self.LOGOUT_LINK)
        logger.info("User logged out.")

    def click_on_home_button(self):
        """
        Clicks on the 'Home' link in the top bar to navigate to the home page.
        Waits for the page to load and logs the action.
        """
        logger.info("Clicking on the 'Home' button in the top bar.")
        self.click(self.HOME_LINK)
        self.page.wait_for_selector('.col-lg-9', state='attached')
        logger.info("Navigated to the home page.")
