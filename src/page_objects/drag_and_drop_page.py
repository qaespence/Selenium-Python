from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class DragAndDropPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/drag_and_drop"
        self.column_a = (By.ID, "column-a")
        self.column_b = (By.ID, "column-b")

    def navigate_to_page(self):
        self.driver.get(self.url)

    def get_column_a_text(self):
        return self.driver.find_element(*self.column_a).text

    def get_column_b_text(self):
        return self.driver.find_element(*self.column_b).text

    def drag_and_drop(self):
        source = self.driver.find_element(*self.column_a)
        target = self.driver.find_element(*self.column_b)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
