from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InputsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/inputs"
        self.input_field = (By.TAG_NAME, "input")

    def navigate_to_page(self):
        self.driver.get(self.url)

    def enter_input_value(self, value):
        input_element = self.driver.find_element(*self.input_field)
        input_element.clear()  # Clear any existing input
        input_element.send_keys(str(value))  # Input the value as a string

    def get_input_value(self):
        input_element = self.driver.find_element(*self.input_field)
        return input_element.get_attribute("value")

    def increase_value_with_arrow_up(self, times=1):
        input_element = self.driver.find_element(*self.input_field)
        for _ in range(times):
            input_element.send_keys(Keys.ARROW_UP)

    def decrease_value_with_arrow_down(self, times=1):
        input_element = self.driver.find_element(*self.input_field)
        for _ in range(times):
            input_element.send_keys(Keys.ARROW_DOWN)
