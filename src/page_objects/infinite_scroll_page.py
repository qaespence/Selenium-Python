from selenium.webdriver.common.by import By
import time


class InfiniteScrollPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/infinite_scroll"
        self.paragraphs = (By.CSS_SELECTOR, "div.jscroll-inner div")

    def navigate_to_page(self):
        self.driver.get(self.url)

    def get_paragraphs_count(self):
        # Return the number of paragraph divs currently loaded
        return len(self.driver.find_elements(*self.paragraphs))

    def scroll_to_bottom(self):
        # Use JavaScript to scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Small pause to allow the content to load
