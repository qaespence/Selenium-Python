import pytest
from src.core.web_driver import initialize_driver
from src.page_objects.notification_message_page import NotificationMessagePage
import time


# Initialize the web driver
@pytest.fixture(scope="module")
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_notification_displayed(driver):
    page = NotificationMessagePage(driver)
    page.navigate_to_page()

    # Trigger the notification by clicking the link
    page.click_link_to_trigger_notification()

    # Verify that the notification is displayed
    assert page.is_notification_displayed(), "Notification message should be displayed after clicking the link."


def test_random_notification_message(driver):
    page = NotificationMessagePage(driver)
    page.navigate_to_page()

    # Define expected messages
    expected_messages = {
        "Action successful",
        "Action unsuccesful, please try again"
    }

    # To track the messages we have seen
    seen_messages = set()

    # Define the maximum number of iterations and a timeout period (in seconds)
    max_iterations = 30
    timeout = 10
    start_time = time.time()

    for _ in range(max_iterations):
        # If all messages have been seen, we can break out early
        if seen_messages == expected_messages:
            break

        # Trigger the notification and capture the message
        page.click_link_to_trigger_notification()
        notification_text = page.get_notification_text().split('\n')[0]  # Get the first line of the notification

        # Check if the notification message is one of the expected messages
        if notification_text in expected_messages:
            seen_messages.add(notification_text)

        # If the timeout is reached, exit the loop
        if time.time() - start_time > timeout:
            break

    # Assert that we have seen all the expected messages
    assert seen_messages == expected_messages, (
        f"Expected messages: {expected_messages} but only saw: {seen_messages}"
    )
