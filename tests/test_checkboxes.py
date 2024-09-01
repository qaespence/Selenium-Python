import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.checkboxes_page import CheckboxesPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_checkboxes_initial_state(driver):
    page = CheckboxesPage(driver)
    page.navigate_to_page()

    # Verify the initial state of the checkboxes
    assert not page.is_checkbox_selected(0), "Checkbox 1 should be unchecked initially."
    assert page.is_checkbox_selected(1), "Checkbox 2 should be checked initially."


def test_select_checkbox(driver):
    page = CheckboxesPage(driver)
    page.navigate_to_page()

    # Select the first checkbox and verify
    page.select_checkbox(0)
    assert page.is_checkbox_selected(0), "Checkbox 1 should be checked after selecting it."


def test_deselect_checkbox(driver):
    page = CheckboxesPage(driver)
    page.navigate_to_page()

    # Deselect the second checkbox and verify
    page.deselect_checkbox(1)
    assert not page.is_checkbox_selected(1), "Checkbox 2 should be unchecked after deselecting it."
