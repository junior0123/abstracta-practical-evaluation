from .base_page import BasePage
from utils.logger_config import setup_logger

# Setting up the logger
logger = setup_logger()

class ProductPage(BasePage):
    """This class represents a product page and provides methods for interacting with the 'Add to Cart' button and handling alerts."""

    ADD_TO_CART_BUTTON = ".btn.btn-success"

    def click_on_add_to_cart_button(self):
        """
        Waits for the 'Add to Cart' button to be visible, clicks it, and handles the confirmation dialog that appears.
        The dialog is accepted automatically after the button is clicked.

        This method ensures that the dialog appears and the alert is handled without errors.
        """
        logger.info("Waiting for the 'Add to Cart' button to become visible.")
        self.page.wait_for_selector(self.ADD_TO_CART_BUTTON, state="visible")
        
        logger.info("Clicking the 'Add to Cart' button.")
        with self.page.expect_event("dialog") as dialog_info:
            self.click(self.ADD_TO_CART_BUTTON)
        
        dialog = dialog_info.value
        self._handle_alert(dialog)
        logger.info("Dialog confirmed after clicking 'Add to Cart'.")

    def _handle_alert(self, dialog):
        """
        Handles the dialog that appears after clicking the 'Add to Cart' button.
        Accepts the dialog automatically.

        Args:
            dialog: The dialog object to be handled.
        """
        logger.info("Handling alert dialog.")
        dialog.accept()
        logger.info("Alert dialog accepted.")
