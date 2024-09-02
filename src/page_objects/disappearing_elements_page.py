from selenium.webdriver.common.by import By


class DisappearingElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/disappearing_elements"
        self.menu_items = (By.CSS_SELECTOR, "ul li a")

    def navigate_to_page(self):
        self.driver.get(self.url)

    def get_menu_items(self):
        return self.driver.find_elements(*self.menu_items)

    def get_menu_item_texts(self):
        return [item.text for item in self.get_menu_items()]

    def click_menu_item_by_text(self, text):
        for item in self.get_menu_items():
            if item.text == text:
                item.click()
                return True
        return False

    def is_menu_item_present(self, text):
        return text in self.get_menu_item_texts()
