from playwright.sync_api import Locator

def scroll_into_view(locator: Locator):
    locator.evaluate("element => element.scrollIntoView({ behavior: 'smooth', block: 'center' })")
