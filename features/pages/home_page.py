from .base_page import BasePage
from playwright.sync_api import expect
from utils.utils import *
from utils.logger_config import setup_logger

# Setting up the logger
logger = setup_logger()

class LoginPage(BasePage):
    """This class represents the login page and contains actions for logging in and interacting with login components."""

    USERNAME_FIELD = "#loginusername"
    PASSWORD_FIELD = "#loginpassword"
    LOGIN_BUTTON = 'button[onclick="logIn()"]'

    def login(self, username: str, password: str):
        """
        Fills in the login form and clicks the login button.
        
        Args:
            username (str): The username for login.
            password (str): The password for login.
        """
        logger.info(f"Attempting to log in with username: {username}")
        self.fill_text(self.USERNAME_FIELD, username)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        logger.info("Login button clicked")

    def click_on_cancel_button(self):
        """Clicks on the cancel (close) button to exit the login form."""
        logger.info("Clicking on cancel button to close the login form.")
        self.page.get_by_label("Log in").get_by_text("Close").click()

    def navigate(self, url: str):
        """
        Navigates to the specified URL and waits for the login page to load.
        
        Args:
            url (str): The URL to navigate to.
        """
        logger.info(f"Navigating to URL: {url}")
        super().navigate(url)
        expect(self.page.locator("#tbodyid")).to_be_visible()
      

class HomePage(BasePage):
    """This class represents the homepage and contains actions for interacting with items and navigating through pages."""

    NEXT_PAGE_BUTTON = "button#next2"
    PREVIOUS_PAGE_BUTTON = "#prev2"

    def click_on_next_button(self):
        """Clicks on the 'Next' button to navigate to the next page."""
        logger.info("Clicking on the 'Next' button.")
        self.click(self.NEXT_PAGE_BUTTON)

    def click_on_previous_button(self):
        """Clicks on the 'Previous' button to navigate to the previous page."""
        logger.info("Clicking on the 'Previous' button.")
        self.click(self.PREVIOUS_PAGE_BUTTON)

    def click_on_select_item(self, item_name: str):
        """
        Clicks on an item by its name to view more details.
        
        Args:
            item_name (str): The name of the item to select.
        """
        logger.info(f"Selecting item: {item_name}")
        item_selector = f'.card-title a:has-text("{item_name}")'
        self.click(item_selector)

    def extract_data_of_all_items(self):
        """Extracts the name, price, and link of all items on the current page and saves it to a text file."""
        logger.info("Extracting data for all items on the current page.")
        self.page.wait_for_selector('.col-lg-9', state='attached')
        self.page.wait_for_selector(".card-block", state='visible')
        self.page.wait_for_selector(".card-title a").wait_for_element_state('stable')
        
        product_names = self.page.locator(".card-title a")
        product_prices = self.page.locator(".card-block h5")
        
        with open("scraped_data.txt", "a") as file:
            if file.tell() == 0:
                file.write("Articles:\n")
            
            for i in range(product_names.count()):
                scroll_into_view(product_names.nth(i))
                name = product_names.nth(i).inner_text()
                price = product_prices.nth(i).inner_text()
                link = product_names.nth(i).get_attribute("href")
                
                file.write(f"{name} - {price} - https://www.demoblaze.com/{link}\n")
                logger.info(f"Extracted data: {name} - {price} - https://www.demoblaze.com/{link}")

    def navigate_through_product_pages(self, number_pages: int):
        """
        Navigates through multiple product pages and extracts data from each page.
        
        Args:
            number_pages (int): The number of pages to navigate through.
        """
        logger.info(f"Starting to navigate through {number_pages} product pages.")
        expect(self.page.locator("#tbodyid")).to_be_visible()
        for page_number in range(number_pages):
            logger.info(f"Extracting data from page {page_number + 1}.")
            self.extract_data_of_all_items()
            if self.page.locator(self.NEXT_PAGE_BUTTON).is_visible():
                self.click_on_next_button()
                logger.info(f"Moved to the next page ({page_number + 2}).")
            else:
                logger.warning("Next button is not visible, stopping pagination.")
                break
