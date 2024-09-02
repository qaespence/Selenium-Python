import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.disappearing_elements_page import DisappearingElementsPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_menu_items_present(driver):
    page = DisappearingElementsPage(driver)
    page.navigate_to_page()

    # Verify that the expected menu items are present
    expected_menu_items = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]
    actual_menu_items = page.get_menu_item_texts()

    for item in expected_menu_items:
        assert item in actual_menu_items, f"Menu item '{item}' should be present."


def test_menu_item_disappearance(driver):
    page = DisappearingElementsPage(driver)
    page.navigate_to_page()

    # Refresh the page multiple times to see if any menu item disappears
    found_missing_item = False
    for _ in range(10):  # Try refreshing the page multiple times
        driver.refresh()
        actual_menu_items = page.get_menu_item_texts()
        if len(actual_menu_items) < 5:
            found_missing_item = True
            break

    assert found_missing_item, "At least one menu item should disappear after refreshing."


def test_click_menu_items(driver):
    page = DisappearingElementsPage(driver)
    page.navigate_to_page()

    # Verify that clicking on each menu item navigates to the correct page
    menu_items = page.get_menu_item_texts()

    for item in menu_items:
        page.click_menu_item_by_text(item)
        assert driver.current_url != page.url, f"Clicking on '{item}' should navigate to a different page."
        driver.back()  # Navigate back to the menu page after each click
