from selenium.webdriver.common.by import By


class CheckboxesPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/checkboxes"
        self.checkbox_elements = (By.CSS_SELECTOR, "input[type='checkbox']")

    def navigate_to_page(self):
        self.driver.get(self.url)

    def get_checkboxes(self):
        return self.driver.find_elements(*self.checkbox_elements)

    def is_checkbox_selected(self, index):
        checkboxes = self.get_checkboxes()
        if 0 <= index < len(checkboxes):
            return checkboxes[index].is_selected()
        else:
            raise IndexError(f"Checkbox index {index} is out of range.")

    def select_checkbox(self, index):
        checkboxes = self.get_checkboxes()
        if 0 <= index < len(checkboxes):
            if not checkboxes[index].is_selected():
                checkboxes[index].click()
        else:
            raise IndexError(f"Checkbox index {index} is out of range.")

    def deselect_checkbox(self, index):
        checkboxes = self.get_checkboxes()
        if 0 <= index < len(checkboxes):
            if checkboxes[index].is_selected():
                checkboxes[index].click()
        else:
            raise IndexError(f"Checkbox index {index} is out of range.")
