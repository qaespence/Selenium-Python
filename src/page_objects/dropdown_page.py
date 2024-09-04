from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DropdownPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/dropdown"
        self.dropdown_element = (By.ID, "dropdown")

    def navigate_to_page(self):
        self.driver.get(self.url)

    def select_option_by_value(self, value):
        dropdown = Select(self.driver.find_element(*self.dropdown_element))
        dropdown.select_by_value(value)

    def select_option_by_visible_text(self, text):
        dropdown = Select(self.driver.find_element(*self.dropdown_element))
        dropdown.select_by_visible_text(text)

    def get_selected_option_text(self):
        dropdown = Select(self.driver.find_element(*self.dropdown_element))
        return dropdown.first_selected_option.text

    def get_all_options_text(self):
        dropdown = Select(self.driver.find_element(*self.dropdown_element))
        return [option.text for option in dropdown.options]
