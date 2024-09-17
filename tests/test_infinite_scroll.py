import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.infinite_scroll_page import InfiniteScrollPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_infinite_scroll_loading(driver):
    page = InfiniteScrollPage(driver)
    page.navigate_to_page()

    # Initial paragraph count
    initial_count = page.get_paragraphs_count()

    # Scroll to the bottom multiple times to trigger more content loading
    scroll_times = 3  # Number of times to scroll down
    for _ in range(scroll_times):
        page.scroll_to_bottom()

    # Final paragraph count after scrolling
    final_count = page.get_paragraphs_count()

    # Verify that more paragraphs have been loaded
    assert final_count > initial_count, f"Expected more paragraphs to be loaded, but found {final_count}"
