import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.shifting_content_menu_page import ShiftingContentMenuPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_default_menu(driver):
    page = ShiftingContentMenuPage(driver)
    url = "https://the-internet.herokuapp.com/shifting_content/menu"
    page.navigate_to_page(url)

    # Verify that there are 5 menu items on the default page
    menu_item_count = page.get_menu_item_count()
    assert menu_item_count == 5, f"Expected 5 menu items, but found {menu_item_count}"

    # Verify the menu item texts
    expected_items = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]
    actual_items = page.get_menu_item_texts()
    assert expected_items == actual_items, f"Expected items {expected_items} but got {actual_items}"


def test_random_menu(driver):
    page = ShiftingContentMenuPage(driver)
    url = "https://the-internet.herokuapp.com/shifting_content/menu?mode=random"
    page.navigate_to_page(url)

    # Check if the menu items still have the expected count and texts (should remain the same)
    menu_item_count = page.get_menu_item_count()
    assert menu_item_count == 5, f"Expected 5 menu items, but found {menu_item_count}"

    expected_items = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]
    actual_items = page.get_menu_item_texts()
    assert expected_items == actual_items, f"Expected items {expected_items} but got {actual_items}"


def test_pixel_shift_menu(driver):
    page = ShiftingContentMenuPage(driver)
    url = "https://the-internet.herokuapp.com/shifting_content/menu?pixel_shift=100"
    page.navigate_to_page(url)

    # Verify that the content is present and menu items are visible even with the pixel shift
    menu_item_count = page.get_menu_item_count()
    assert menu_item_count == 5, f"Expected 5 menu items, but found {menu_item_count}"

    expected_items = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]
    actual_items = page.get_menu_item_texts()
    assert expected_items == actual_items, f"Expected items {expected_items} but got {actual_items}"


def test_random_and_pixel_shift_menu(driver):
    page = ShiftingContentMenuPage(driver)
    url = "https://the-internet.herokuapp.com/shifting_content/menu?mode=random&pixel_shift=100"
    page.navigate_to_page(url)

    # Verify that the menu items are present with the random mode and pixel shift
    menu_item_count = page.get_menu_item_count()
    assert menu_item_count == 5, f"Expected 5 menu items, but found {menu_item_count}"

    expected_items = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]
    actual_items = page.get_menu_item_texts()
    assert expected_items == actual_items, f"Expected items {expected_items} but got {actual_items}"


def test_dynamic_pixel_shift(driver):
    page = ShiftingContentMenuPage(driver)

    # Test for multiple pixel_shift values
    pixel_shift_values = [50, 100, 150, 200]
    for shift_value in pixel_shift_values:
        url = f"https://the-internet.herokuapp.com/shifting_content/menu?pixel_shift={shift_value}"
        page.navigate_to_page(url)

        # Verify the menu items are present with the dynamic pixel shift
        menu_item_count = page.get_menu_item_count()
        assert menu_item_count == 5, f"Expected 5 menu items with pixel shift {shift_value}, but found {menu_item_count}"

        expected_items = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]
        actual_items = page.get_menu_item_texts()
        assert expected_items == actual_items, f"Expected items {expected_items} with pixel shift {shift_value} but got {actual_items}"
