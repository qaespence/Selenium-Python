from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HorizontalSliderPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/horizontal_slider"
        self.slider = (By.CSS_SELECTOR, "input[type='range']")
        self.slider_value = (By.ID, "range")

    def navigate_to_page(self):
        self.driver.get(self.url)

    def get_slider_value(self):
        # Return the current value displayed on the slider
        return self.driver.find_element(*self.slider_value).text

    def move_slider_by_mouse(self, offset):
        # Move the slider by dragging with the mouse
        slider_element = self.driver.find_element(*self.slider)
        actions = ActionChains(self.driver)
        actions.click_and_hold(slider_element).move_by_offset(offset, 0).release().perform()

    def move_slider_by_keyboard(self, key):
        # Move the slider using keyboard input without clicking the slider first
        slider_element = self.driver.find_element(*self.slider)
        slider_element.send_keys(key)  # Send the key input (Keys.ARROW_LEFT or Keys.ARROW_RIGHT)
