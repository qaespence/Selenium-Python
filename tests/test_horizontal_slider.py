import pytest
from selenium.webdriver.common.keys import Keys
from src.core.web_driver import initialize_driver
from src.page_objects.horizontal_slider_page import HorizontalSliderPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_slider_move_by_mouse(driver):
    page = HorizontalSliderPage(driver)
    page.navigate_to_page()

    # Get the initial value of the slider
    initial_value = page.get_slider_value()

    # Move the slider to the right by a certain offset (e.g., 50 pixels)
    page.move_slider_by_mouse(50)

    # Get the value of the slider after moving
    after_move_value = page.get_slider_value()

    # Verify that the slider value has changed after moving with the mouse
    assert initial_value != after_move_value, f"Expected slider value to change after moving, but it remained {initial_value}"


def test_slider_move_by_keyboard(driver):
    page = HorizontalSliderPage(driver)
    page.navigate_to_page()

    # Get the initial value of the slider
    initial_value = page.get_slider_value()

    # Move the slider to the right using the keyboard (right arrow key)
    page.move_slider_by_keyboard(Keys.ARROW_RIGHT)

    # Get the value of the slider after pressing the right arrow key
    after_key_move_value = page.get_slider_value()

    # Verify that the slider value has changed after using the keyboard
    assert initial_value != after_key_move_value, f"Expected slider value to change after using the keyboard, but it remained {initial_value}"


def test_slider_move_to_max_and_min_by_keyboard(driver):
    page = HorizontalSliderPage(driver)
    page.navigate_to_page()

    # Move the slider to the right by pressing the right arrow key until it reaches the max value (5)
    max_value = None
    max_retries = 100  # Emergency break if we hit the right arrow too many times
    counter = 0
    while True:
        page.move_slider_by_keyboard(Keys.ARROW_RIGHT)
        max_value = page.get_slider_value()
        if max_value == "5" or counter >= max_retries:
            break
        counter += 1

    # Verify that the slider has reached the maximum value (5)
    assert max_value == "5", f"Expected slider value to be 5, but it was {max_value}"

    # Now move the slider to the left by pressing the left arrow key until it reaches the min value (0)
    min_value = None
    min_retries = 100  # Emergency break if we hit the left arrow too many times
    counter = 0
    while True:
        page.move_slider_by_keyboard(Keys.ARROW_LEFT)
        min_value = page.get_slider_value()
        if min_value == "0" or counter >= min_retries:
            break
        counter += 1

    # Verify that the slider has reached the minimum value (0)
    assert min_value == "0", f"Expected slider value to be 0, but it was {min_value}"
