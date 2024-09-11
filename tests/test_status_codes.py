import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.status_codes_page import StatusCodesPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


@pytest.mark.parametrize("status_code, expected_message_part", [
    ("200", "This page returned a 200 status code."),
    ("301", "This page returned a 301 status code."),
    ("404", "This page returned a 404 status code."),
    ("500", "This page returned a 500 status code."),
])
def test_status_code_links(driver, status_code, expected_message_part):
    page = StatusCodesPage(driver)
    page.navigate_to_page()

    # Click on the status code link
    page.click_status_code_link(status_code)

    # Verify the URL has the correct status code at the end
    assert status_code in page.get_current_url(), f"URL should contain {status_code}"

    # Verify that the correct status message is displayed on the page
    status_message = page.get_status_message_text()
    assert expected_message_part in status_message, f"Expected message '{expected_message_part}', but got '{status_message}'"
