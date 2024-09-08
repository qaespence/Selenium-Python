from selenium.webdriver.common.by import By


class ShiftingContentMenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_items = (By.CSS_SELECTOR, "div#content ul li")

    def navigate_to_page(self, url):
        self.driver.get(url)

    def get_menu_items(self):
        # Find all the menu items in the list
        return self.driver.find_elements(*self.menu_items)

    def get_menu_item_texts(self):
        # Return the text of all menu items
        return [item.text for item in self.get_menu_items()]

    def get_menu_item_count(self):
        # Return the count of menu items
        return len(self.get_menu_items())
