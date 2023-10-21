from selenium.webdriver.common.by import By


class BrokenImagesPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/broken_images"
        self.image_elements = (By.TAG_NAME, "img")

    def navigate_to_page(self):
        self.driver.get(self.url)

    def get_broken_images(self):
        images = self.driver.find_elements(*self.image_elements)
        broken_images = []

        for image in images:
            response_code = self.get_image_response_code(image.get_attribute("src"))
            if response_code != 200:
                broken_images.append(image.get_attribute("src"))

        return broken_images

    def get_image_response_code(self, image_url):
        import requests
        response = requests.head(image_url)
        return response.status_code
