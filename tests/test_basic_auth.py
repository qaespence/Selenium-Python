import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.basic_auth_page import BasicAuthPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_successful_login(driver):
    page = BasicAuthPage(driver)
    page.navigate_to_page()

    # Verify that the login was successful
    assert page.is_successful_login()
