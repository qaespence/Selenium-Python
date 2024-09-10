import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.shifting_content_list_page import ShiftingContentListPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


@pytest.mark.skip(reason="This test is currently skipped due to a bad/invalid selector for the list")
def test_default_list_items(driver):
    page = ShiftingContentListPage(driver)
    page.navigate_to_page()

    # Verify that there are 5 list items on the page
    list_item_count = page.get_list_item_count()
    assert list_item_count == 5, f"Expected 5 list items, but found {list_item_count}"

    # Verify the text of the list items
    expected_items = [
        "Important Information You're Looking For",
        "Et numquam et aliquam.",
        "Nesciunt autem eum odit fuga tempora deleniti.",
        "Sed deleniti blanditiis odio laudantium.",
        "Vel aliquid dolores veniam enim nesciunt libero quaerat."
    ]
    actual_items = set(page.get_list_item_texts())
    assert expected_items == actual_items, f"Expected items {expected_items} but got {actual_items}"


def test_list_item_visibility(driver):
    page = ShiftingContentListPage(driver)
    page.navigate_to_page()

    # Verify that all list items are visible on the page
    list_items = page.get_list_items()
    all_visible = all(item.is_displayed() for item in list_items)
    assert all_visible, "Not all list items are visible."


def test_list_item_layout_stability(driver):
    page = ShiftingContentListPage(driver)
    page.navigate_to_page()

    # Capture the original location of each list item
    original_positions = [item.location for item in page.get_list_items()]

    # Refresh the page to check if the layout shifts
    driver.refresh()

    # Capture the new location of each list item
    new_positions = [item.location for item in page.get_list_items()]

    # Verify that the positions of list items remain the same
    assert original_positions == new_positions, "List item positions shifted after page refresh."
