from selenium.webdriver.common.by import By


class KeyPressesPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/key_presses"
        self.result_text = (By.ID, "result")
        self.input_field = (By.TAG_NAME, "body")  # The body captures key presses in this case

    def navigate_to_page(self):
        self.driver.get(self.url)

    def press_key(self, key):
        input_element = self.driver.find_element(*self.input_field)
        input_element.send_keys(key)

    def get_result_text(self):
        return self.driver.find_element(*self.result_text).text
