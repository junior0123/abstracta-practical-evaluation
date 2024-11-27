from .base_page import BasePage
from utils.logger_config import setup_logger
logger = setup_logger()

class CartPage(BasePage):
    """
    Page object model for the Cart page, which contains methods for interacting with
    the shopping cart in the application.

    Attributes:
        PLACE_ORDER_BUTTON (str): Selector for the place order button.
        NAME_FIELD (str): Selector for the name input field.
        COUNTRY_FIELD (str): Selector for the country input field.
        CITY_FIELD (str): Selector for the city input field.
        CREDIT_CARD_FIELD (str): Selector for the credit card input field.
        MONTH_FIELD (str): Selector for the expiration month input field.
        YEAR_FIELD (str): Selector for the expiration year input field.
        PURCHASE_ORDER_BUTTON (str): Selector for the purchase order button.
        CONFIRMATION_ORDER_BUTTON (str): Selector for the confirmation order button.
    """
    
    PLACE_ORDER_BUTTON = ".btn.btn-success"
    NAME_FIELD = "#name"
    COUNTRY_FIELD = "#country"
    CITY_FIELD = "#city"
    CREDIT_CARD_FIELD = "#card"
    MONTH_FIELD = "#month"
    YEAR_FIELD = "#year"
    PURCHASE_ORDER_BUTTON = 'button[onclick="purchaseOrder()"]'
    CONFIRMATION_ORDER_BUTTON = ".confirm.btn.btn-lg.btn-primary"

    def click_on_place_order_button(self):
        """
        Clicks on the 'Place Order' button to initiate the order process.
        Logs the action.

        Returns:
            None
        """
        logger.info("Clicking on the 'Place Order' button.")
        self.click(self.PLACE_ORDER_BUTTON)

    def fill_order_information(self, name, country, city, credit_card_number, month, year):
        """
        Fills the order form with the provided customer details.

        Args:
            name (str): The customer's name.
            country (str): The customer's country.
            city (str): The customer's city.
            credit_card_number (str): The customer's credit card number.
            month (str): The credit card expiration month.
            year (str): The credit card expiration year.

        Returns:
            None
        """
        logger.info(f"Filling order information for: {name}, {country}, {city}, {credit_card_number}, {month}, {year}")
        self.fill_text(self.NAME_FIELD, name)
        self.fill_text(self.COUNTRY_FIELD, country)
        self.fill_text(self.CITY_FIELD, city)
        self.fill_text(self.CREDIT_CARD_FIELD, credit_card_number)
        self.fill_text(self.MONTH_FIELD, month)
        self.fill_text(self.YEAR_FIELD, year)

    def click_on_purchase_order_button(self):
        """
        Clicks on the 'Purchase Order' button to complete the order.

        Waits for the page to load and verifies that the order modal is visible.

        Returns:
            None
        """
        logger.info("Clicking on the 'Purchase Order' button.")
        self.page.wait_for_load_state('load')
        self.click(self.PURCHASE_ORDER_BUTTON)
        assert self.page.locator("#orderModal .modal-dialog .modal-content").is_visible()
        logger.info("Order modal is visible after clicking 'Purchase Order'.")

    def click_on_confirmation_order_button(self):
        """
        Clicks on the 'Confirm Order' button to finalize the order.

        Returns:
            None
        """
        logger.info("Clicking on the 'Confirm Order' button.")
        self.click(self.CONFIRMATION_ORDER_BUTTON)

    def verify_exist_item(self, item_name):
        """
        Verifies that an item is present in the cart.

        Args:
            item_name (str): The name of the item to verify.

        Returns:
            None
        """
        item_selector = f'//tbody[@id="tbodyid"]/tr/td[2][text()="{item_name}"]'
        logger.info(f"Verifying if item '{item_name}' exists in the cart.")
        self.page.wait_for_selector(".table-responsive")
        self.page.wait_for_load_state('load')
        self.page.wait_for_selector(item_selector, state='visible')
        assert self.page.locator(item_selector).is_visible(), f"Product '{item_name}' not found in the cart"
        logger.info(f"Product '{item_name}' found in the cart.")

    def verify_item_not_exist(self, item_name):
        """
        Verifies that an item is not present in the cart.

        Args:
            item_name (str): The name of the item to verify.

        Returns:
            None
        """
        item_selector = f'//tbody[@id="tbodyid"]/tr/td[2][text()="{item_name}"]'
        logger.info(f"Verifying if item '{item_name}' does not exist in the cart.")
        self.page.wait_for_selector(".table-responsive")
        self.page.wait_for_load_state('load')
        assert self.page.locator(item_selector).count() == 0, f"Product '{item_name}' was found in the cart but shouldn't be."
        logger.info(f"Product '{item_name}' is not in the cart.")

    def delete_selected_item_from_cart(self, item_name):
        """
        Deletes the selected item from the cart.

        Args:
            item_name (str): The name of the item to delete.

        Returns:
            None
        """
        delete_item_selector = f'//tbody[@id="tbodyid"]/tr[td[2][text()="{item_name}"]]/td[4]/a'
        logger.info(f"Deleting item '{item_name}' from the cart.")
        self.page.wait_for_selector(delete_item_selector, state='visible')
        self.click(delete_item_selector)
        logger.info(f"Item '{item_name}' deleted from the cart.")

    def verify_order_information(self):
        """
        Verifies the order information after submission, specifically the confirmation modal.

        Returns:
            None
        """
        ALERT_SELECTOR = ".sweet-alert.showSweetAlert.visible"
        logger.info("Verifying order confirmation information.")
        self.page.wait_for_selector(ALERT_SELECTOR, state='visible')
        alert_locator = self.page.locator(ALERT_SELECTOR)
        header_text = alert_locator.locator("h2").text_content()
        assert header_text == "Thank you for your purchase!", f"Expected header text 'Thank you for your purchase!' but got '{header_text}'"
        logger.info("Order confirmation verified successfully.")

    def verify_quantity_of_products_in_the_cart(self):
        """
        Verifies the quantity of products in the cart.

        Returns:
            None
        """
        rows_selector = '//tbody[@id="tbodyid"]/tr'
        logger.info("Verifying the quantity of products in the cart.")
        self.page.wait_for_selector(rows_selector)
        actual_count = self.page.locator(rows_selector).count()
        assert actual_count == 1, f"Expected 1 item in the cart, but found {actual_count}."
        logger.info(f"Cart contains {actual_count} item(s), as expected.")
