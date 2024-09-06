import pytest
from selenium.webdriver.common.keys import Keys
from src.core.web_driver import initialize_driver
from src.page_objects.key_presses_page import KeyPressesPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_press_enter_key(driver):
    page = KeyPressesPage(driver)
    page.navigate_to_page()

    # Simulate pressing the ENTER key
    page.press_key(Keys.ENTER)

    # Verify the result message
    is_result_correct = "You entered: ENTER" in page.get_result_text()
    assert is_result_correct, f"Expected result to be 'You entered: ENTER' but got '{page.get_result_text()}'"


def test_press_space_key(driver):
    page = KeyPressesPage(driver)
    page.navigate_to_page()

    # Simulate pressing the SPACE key
    page.press_key(Keys.SPACE)

    # Verify the result message
    is_result_correct = "You entered: SPACE" in page.get_result_text()
    assert is_result_correct, f"Expected result to be 'You entered: SPACE' but got '{page.get_result_text()}'"


def test_press_shift_key(driver):
    page = KeyPressesPage(driver)
    page.navigate_to_page()

    # Simulate pressing the SHIFT key
    page.press_key(Keys.SHIFT)

    # Verify the result message
    is_result_correct = "You entered: SHIFT" in page.get_result_text()
    assert is_result_correct, f"Expected result to be 'You entered: SHIFT' but got '{page.get_result_text()}'"


def test_press_any_letter_key(driver):
    page = KeyPressesPage(driver)
    page.navigate_to_page()

    # Simulate pressing the "A" key
    page.press_key("A")

    # Verify the result message
    is_result_correct = "You entered: A" in page.get_result_text()
    assert is_result_correct, f"Expected result to be 'You entered: A' but got '{page.get_result_text()}'"
