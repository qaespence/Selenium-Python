import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.drag_and_drop_page import DragAndDropPage


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_initial_positions(driver):
    page = DragAndDropPage(driver)
    page.navigate_to_page()

    # Verify initial positions
    is_column_a_correct = page.get_column_a_text() == "A"
    is_column_b_correct = page.get_column_b_text() == "B"

    assert is_column_a_correct and is_column_b_correct, (
        f"Initial state failed: Column A: {page.get_column_a_text()}, "
        f"Column B: {page.get_column_b_text()}"
    )


def test_drag_and_drop_operation(driver):
    page = DragAndDropPage(driver)
    page.navigate_to_page()

    # Perform drag and drop
    page.drag_and_drop()

    # Verify positions after drag and drop
    is_column_a_correct = page.get_column_a_text() == "B"
    is_column_b_correct = page.get_column_b_text() == "A"

    assert is_column_a_correct and is_column_b_correct, (
        f"Drag and drop failed: Column A: {page.get_column_a_text()}, "
        f"Column B: {page.get_column_b_text()}"
    )


def test_drag_and_drop_reversibility(driver):
    page = DragAndDropPage(driver)
    page.navigate_to_page()

    # Perform drag and drop twice to return to the original position
    page.drag_and_drop()
    page.drag_and_drop()

    # Verify positions are back to the initial state
    is_column_a_correct = page.get_column_a_text() == "A"
    is_column_b_correct = page.get_column_b_text() == "B"

    assert is_column_a_correct and is_column_b_correct, (
        f"Drag and drop reversibility failed: Column A: {page.get_column_a_text()}, "
        f"Column B: {page.get_column_b_text()}"
    )
