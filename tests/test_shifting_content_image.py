import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.shifting_content_image_page import ShiftingContentImagePage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_default_image_display(driver):
    page = ShiftingContentImagePage(driver)
    url = "https://the-internet.herokuapp.com/shifting_content/image"
    page.navigate_to_page(url)

    # Verify that the image is displayed
    assert page.is_image_displayed(), "Image should be displayed."


def test_random_mode_image(driver):
    page = ShiftingContentImagePage(driver)
    url = "https://the-internet.herokuapp.com/shifting_content/image?mode=random"
    page.navigate_to_page(url)

    # Verify that the image is displayed in random mode
    assert page.is_image_displayed(), "Image should be displayed in random mode."


def test_pixel_shift_image(driver):
    page = ShiftingContentImagePage(driver)
    url = "https://the-internet.herokuapp.com/shifting_content/image?pixel_shift=100"
    page.navigate_to_page(url)

    # Verify that the image is displayed with pixel shift
    assert page.is_image_displayed(), "Image should be displayed with pixel shift."

    # Check the image dimensions to confirm that pixel shift had an effect (dimensions might change based on implementation)
    width, height = page.get_image_dimensions()
    assert width > 0 and height > 0, f"Image dimensions should be valid, got width: {width}, height: {height}"


def test_random_mode_and_pixel_shift_image(driver):
    page = ShiftingContentImagePage(driver)
    url = "https://the-internet.herokuapp.com/shifting_content/image?mode=random&pixel_shift=100"
    page.navigate_to_page(url)

    # Verify that the image is displayed with random mode and pixel shift
    assert page.is_image_displayed(), "Image should be displayed with random mode and pixel shift."


def test_simple_image_type(driver):
    page = ShiftingContentImagePage(driver)
    url = "https://the-internet.herokuapp.com/shifting_content/image?image_type=simple"
    page.navigate_to_page(url)

    # Verify that the image is displayed with simple image type
    assert page.is_image_displayed(), "Simple image should be displayed."


def test_dynamic_pixel_shift(driver):
    page = ShiftingContentImagePage(driver)

    # Test for multiple pixel_shift values
    pixel_shift_values = [50, 100, 150, 200]
    for shift_value in pixel_shift_values:
        url = f"https://the-internet.herokuapp.com/shifting_content/image?pixel_shift={shift_value}"
        page.navigate_to_page(url)

        # Verify that the image is displayed with the dynamic pixel shift
        assert page.is_image_displayed(), f"Image should be displayed with pixel shift {shift_value}."

        # Optionally verify image dimensions or other properties
        width, height = page.get_image_dimensions()
        assert width > 0 and height > 0, f"Image dimensions should be valid with pixel shift {shift_value}, got width: {width}, height: {height}"
