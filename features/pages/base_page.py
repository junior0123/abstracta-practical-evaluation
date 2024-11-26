from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.click(locator)

    def fill_text(self, locator: str, text: str):
        self.page.fill(locator, text)
