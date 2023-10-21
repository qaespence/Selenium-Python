import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.add_remove_elements import AddRemoveElementsPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_add_and_remove_elements(driver):
    page = AddRemoveElementsPage(driver)
    page.navigate_to_page()

    # Add elements and verify the count
    page.add_elements(3)
    assert page.get_element_count() == 3

    # Remove elements and verify the count
    page.remove_elements(2)
    assert page.get_element_count() == 1


def test_hover_over_element(driver):
    page = AddRemoveElementsPage(driver)
    page.navigate_to_page()

    # Add elements and hover over the first one
    page.add_elements(2)
    page.hover_over_element(0)

    # Check if the hovered element is visible
    assert page.is_element_visible(0)


def test_get_elements_text(driver):
    page = AddRemoveElementsPage(driver)
    page.navigate_to_page()

    # Add elements and get their text
    page.add_elements(3)
    elements_text = page.get_elements_text()

    assert len(elements_text) == 3
    assert all("Delete" in text for text in elements_text)

    driver.quit()  # Close the browser
