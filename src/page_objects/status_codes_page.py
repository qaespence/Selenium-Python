from selenium.webdriver.common.by import By


class StatusCodesPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/status_codes"
        self.status_code_links = {
            "200": (By.LINK_TEXT, "200"),
            "301": (By.LINK_TEXT, "301"),
            "404": (By.LINK_TEXT, "404"),
            "500": (By.LINK_TEXT, "500")
        }
        self.status_message = (By.TAG_NAME, "p")

    def navigate_to_page(self):
        self.driver.get(self.url)

    def click_status_code_link(self, code):
        # Click on the status code link based on the provided code
        self.driver.find_element(*self.status_code_links[code]).click()

    def get_status_message_text(self):
        # Return the text from the status message on the resulting page
        return self.driver.find_element(*self.status_message).text

    def get_current_url(self):
        # Get the current URL of the page
        return self.driver.current_url
