from selenium.webdriver.common.by import By


class ShiftingContentListPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/shifting_content/list"
        self.list_items = (By.CSS_SELECTOR, "div#content ul li")

    def navigate_to_page(self):
        self.driver.get(self.url)

    def get_list_items(self):
        # Find all the list items in the unordered list
        return self.driver.find_elements(*self.list_items)

    def get_list_item_texts(self):
        # Return the text of all list items
        return [item.text for item in self.get_list_items()]

    def get_list_item_count(self):
        # Return the count of list items
        return len(self.get_list_items())
