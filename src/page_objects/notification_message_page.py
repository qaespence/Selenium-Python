from selenium.webdriver.common.by import By


class NotificationMessagePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/notification_message"
        self.click_link = (By.LINK_TEXT, "Click here")
        self.notification_message = (By.ID, "flash")

    def navigate_to_page(self):
        self.driver.get(self.url)

    def click_link_to_trigger_notification(self):
        self.driver.find_element(*self.click_link).click()

    def get_notification_text(self):
        return self.driver.find_element(*self.notification_message).text.strip()

    def is_notification_displayed(self):
        return self.driver.find_element(*self.notification_message).is_displayed()
