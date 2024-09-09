from selenium.webdriver.common.by import By


class ShiftingContentImagePage:
    def __init__(self, driver):
        self.driver = driver
        self.image_element = (By.TAG_NAME, "img")

    def navigate_to_page(self, url):
        self.driver.get(url)

    def is_image_displayed(self):
        # Check if the image is displayed on the page
        return self.driver.find_element(*self.image_element).is_displayed()

    def get_image_src(self):
        # Get the source URL of the image
        return self.driver.find_element(*self.image_element).get_attribute("src")

    def get_image_dimensions(self):
        # Get the width and height of the image
        image = self.driver.find_element(*self.image_element)
        return image.size['width'], image.size['height']
