from selenium.webdriver.common.by import By


class DynamicContentPage:
    def __init__(self, driver):
        self.driver = driver
        self.url_dynamic = "https://the-internet.herokuapp.com/dynamic_content"
        self.url_static = "https://the-internet.herokuapp.com/dynamic_content?with_content=static"

        self.content_items = (By.CSS_SELECTOR, "div.row > div.large-10.columns")

    def navigate_to_dynamic_content(self):
        self.driver.get(self.url_dynamic)

    def navigate_to_static_content(self):
        self.driver.get(self.url_static)

    def get_content_items(self):
        # Get the full content block and split manually by text structure
        content = [item.text.strip() for item in self.driver.find_elements(*self.content_items)]
        return "\n\n\n".join(content)  # Join them by three newlines to ensure proper splitting

    def get_content_texts(self):
        # Manually split the content by double newline (to handle it as separate blocks)
        full_content = self.get_content_items()
        return full_content.split("\n\n\n")  # Return list of separate content blocks
