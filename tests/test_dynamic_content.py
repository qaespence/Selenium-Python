import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.dynamic_content_page import DynamicContentPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_dynamic_content_changes_on_refresh(driver):
    page = DynamicContentPage(driver)
    page.navigate_to_dynamic_content()

    # Capture the content after the first load
    first_content = page.get_content_texts()

    # Refresh the page to load new dynamic content
    driver.refresh()

    # Capture the content after the refresh
    second_content = page.get_content_texts()

    # Verify that the content has changed after the refresh
    assert first_content != second_content, "Content did not change after refresh."


def test_static_and_dynamic_content_on_refresh(driver):
    page = DynamicContentPage(driver)
    page.navigate_to_static_content()

    # Capture the content after the first load
    first_content = page.get_content_texts()

    # Refresh the page to load the static content again
    driver.refresh()

    # Capture the content after the refresh
    second_content = page.get_content_texts()

    # Split the content into static (first 2 blocks) and dynamic (last block)
    first_static_content = first_content[:2]  # First 2 content blocks (static)
    first_dynamic_content = first_content[2]  # Last block (dynamic)

    second_static_content = second_content[:2]  # First 2 content blocks (static after refresh)
    second_dynamic_content = second_content[2]  # Last block (dynamic after refresh)

    # Combine the assertions into a single assertion for all checks
    all_checks = [
        first_static_content == second_static_content,  # Static content remains the same
        first_dynamic_content != second_dynamic_content  # Dynamic content changes
    ]

    assert all(all_checks), "Static content changed or dynamic content did not change after refresh."
