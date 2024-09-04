import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.dropdown_page import DropdownPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_default_selected_option(driver):
    page = DropdownPage(driver)
    page.navigate_to_page()

    # Verify that the default selected option is "Please select an option"
    is_default_option_correct = page.get_selected_option_text() == "Please select an option"
    assert is_default_option_correct, f"Expected default option to be 'Please select an option' but got '{page.get_selected_option_text()}'"


def test_select_option_by_value(driver):
    page = DropdownPage(driver)
    page.navigate_to_page()

    # Select option 1 by value and verify the selection
    page.select_option_by_value("1")
    is_option_1_selected = page.get_selected_option_text() == "Option 1"
    assert is_option_1_selected, f"Expected 'Option 1' to be selected but got '{page.get_selected_option_text()}'"


def test_select_option_by_visible_text(driver):
    page = DropdownPage(driver)
    page.navigate_to_page()

    # Select Option 2 by visible text and verify the selection
    page.select_option_by_visible_text("Option 2")
    is_option_2_selected = page.get_selected_option_text() == "Option 2"
    assert is_option_2_selected, f"Expected 'Option 2' to be selected but got '{page.get_selected_option_text()}'"


def test_all_options_present(driver):
    page = DropdownPage(driver)
    page.navigate_to_page()

    # Verify that all options are present in the dropdown
    expected_options = ["Please select an option", "Option 1", "Option 2"]
    actual_options = page.get_all_options_text()
    assert expected_options == actual_options, f"Expected options {expected_options} but got {actual_options}"
