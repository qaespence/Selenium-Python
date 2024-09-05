import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.inputs_page import InputsPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_enter_positive_number(driver):
    page = InputsPage(driver)
    page.navigate_to_page()

    # Enter a positive number and verify
    page.enter_input_value(123)
    is_value_correct = page.get_input_value() == "123"
    assert is_value_correct, f"Expected input value to be '123' but got '{page.get_input_value()}'"


def test_enter_negative_number(driver):
    page = InputsPage(driver)
    page.navigate_to_page()

    # Enter a negative number and verify
    page.enter_input_value(-456)
    is_value_correct = page.get_input_value() == "-456"
    assert is_value_correct, f"Expected input value to be '-456' but got '{page.get_input_value()}'"


def test_enter_float_number(driver):
    page = InputsPage(driver)
    page.navigate_to_page()

    # Enter a float number and verify
    page.enter_input_value(78.9)
    is_value_correct = page.get_input_value() == "78.9"
    assert is_value_correct, f"Expected input value to be '78.9' but got '{page.get_input_value()}'"


def test_increase_value_with_arrow_up(driver):
    page = InputsPage(driver)
    page.navigate_to_page()

    # Set the initial value and increase with the up arrow key
    page.enter_input_value(10)
    page.increase_value_with_arrow_up(5)  # Press the up arrow key 5 times

    is_value_correct = page.get_input_value() == "15"
    assert is_value_correct, f"Expected input value to be '15' but got '{page.get_input_value()}'"


def test_decrease_value_with_arrow_down(driver):
    page = InputsPage(driver)
    page.navigate_to_page()

    # Set the initial value and decrease with the down arrow key
    page.enter_input_value(10)
    page.decrease_value_with_arrow_down(3)  # Press the down arrow key 3 times

    is_value_correct = page.get_input_value() == "7"
    assert is_value_correct, f"Expected input value to be '7' but got '{page.get_input_value()}'"


def test_enter_non_numeric_value(driver):
    page = InputsPage(driver)
    page.navigate_to_page()

    # Enter a non-numeric value and verify the field remains empty
    page.enter_input_value("test")
    is_field_empty = page.get_input_value() == ""
    assert is_field_empty, f"Expected input value to be empty but got '{page.get_input_value()}'"
