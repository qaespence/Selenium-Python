import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.broken_images_page import BrokenImagesPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_broken_images(driver):
    page = BrokenImagesPage(driver)
    page.navigate_to_page()

    # Get the list of broken image URLs
    broken_images = page.get_broken_images()

    # Verify that there are 2 broken images
    assert len(broken_images) == 2
