from selenium.webdriver.common.by import By


class BasicAuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/basic_auth"
        self.success_message = (
        By.XPATH, '//p[contains(text(), "Congratulations! You must have the proper credentials.")]')

    def navigate_to_page(self, username="admin", password="admin"):
        # Access the page with the provided username and password in the URL
        self.driver.get(f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth")

    def is_successful_login(self):
        # Check if the success message is displayed
        return self.driver.find_element(*self.success_message).is_displayed()
