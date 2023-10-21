from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class AddRemoveElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_element_button = (By.XPATH, '//*[@onclick="addElement()"]')
        self.delete_element_button = (By.CLASS_NAME, 'added-manually')
        self.elements_list = (By.ID, 'elements')

    def navigate_to_page(self):
        self.driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    def click_add_element_button(self):
        self.driver.find_element(*self.add_element_button).click()

    def click_delete_element_button(self):
        self.driver.find_element(*self.delete_element_button).click()

    def get_element_count(self):
        return len(self.driver.find_elements(*self.delete_element_button))

    def add_elements(self, count):
        for _ in range(count):
            self.click_add_element_button()

    def remove_elements(self, count):
        for _ in range(count):
            if self.get_element_count() > 0:
                self.click_delete_element_button()

    def get_elements_text(self):
        return [element.text for element in self.driver.find_elements(*self.delete_element_button)]

    def hover_over_element(self, index):
        elements = self.driver.find_elements(*self.delete_element_button)
        action = ActionChains(self.driver)
        action.move_to_element(elements[index]).perform()

    def is_element_visible(self, index):
        elements = self.driver.find_elements(*self.delete_element_button)
        return elements[index].is_displayed()
