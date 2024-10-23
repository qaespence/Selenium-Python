# Web Automation Testing Framework

This repository contains a web automation testing framework using **Python**, **Selenium**, and **pytest**. It includes tests for various pages of "The Internet" demo site at https://the-internet.herokuapp.com/.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [Running Tests](#running-tests)
- [File and Folder Structure](#file-and-folder-structure)

---

## Setup Instructions

### Prerequisites

Before setting up the framework, ensure that the following tools are installed on your machine:

1. **Python 3.7+**: Install Python from [python.org](https://www.python.org/downloads/).
2. **pip**: Python's package manager (comes pre-installed with Python).
3. **WebDriver** (e.g., ChromeDriver or GeckoDriver): Required to run Selenium tests on a specific browser.

#### WebDriver Setup:
   - **ChromeDriver**: [Download](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - **GeckoDriver** (for Firefox): [Download](https://github.com/mozilla/geckodriver/releases)
   
   After downloading the WebDriver, make sure it's available in your system's `PATH`.

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-repo-url/web-automation-framework.git
cd web-automation-framework
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)

It is a good practice to create a virtual environment to isolate project dependencies.

#### Create a Virtual Environment:

```bash
python -m venv venv
```

#### Activate the Virtual Environment:

- On Windows:
    ```bash
    venv\Scripts\activate
    ```
- On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

### Step 3: Install Project Dependencies

Install all required packages (Selenium, pytest, etc.) using `pip`:

```bash
pip install -r requirements.txt
```

This command will install the dependencies listed in the `requirements.txt` file, including:
- `selenium`
- `pytest`

---

## Running Tests

Once the environment is set up, you can run the tests using **pytest**.

### Command to Run All Tests:

```bash
pytest
```

### Run a Specific Test File:

```bash
pytest tests/test_notification_message.py
```

### Run Tests with Verbose Output:

```bash
pytest -v
```

### Run Tests in Parallel (Optional, Requires pytest-xdist Plugin):

To run tests in parallel, you can use the `pytest-xdist` plugin. Install it using:

```bash
pip install pytest-xdist
```

Then run the tests with parallelism:

```bash
pytest -n auto
```

---

## File and Folder Structure

Here’s a breakdown of the project's structure:

```
web-automation-framework/
├── src/                         # Contains the core logic and Page Object Model (POM)
│   ├── core/                    # Core setup and WebDriver initialization
│   │   └── web_driver.py        # WebDriver setup logic
│   ├── page_objects/            # Page Object files for different test pages
│   │   ├── dropdown_page.py     # Page object for Dropdown test page
│   │   ├── inputs_page.py       # Page object for Inputs test page│   │   ├── notification_message_page.py  # Page object for Notification Message test page
│   │   └── ...                  # Other page objects for different URLs
├── tests/                       # Test files for each feature
│   ├── test_dropdown.py         # Test file for Dropdown page
│   ├── test_inputs.py           # Test file for Inputs page│   ├── test_notification_message.py  # Test file for Notification Message page
│   └── ...                      # Other test files
├── requirements.txt             # List of project dependencies
├── pytest.ini                   # Pytest configuration file
└── README.md                    # This README file
```

### Explanation of Key Components:

- **`src/core/web_driver.py`:** Contains the logic for initializing the WebDriver (Chrome, Firefox, etc.).
- **`src/page_objects/`:** Houses all Page Object Model (POM) files. Each file represents a page on the test site and includes methods for interacting with page elements.
- **`tests/`:** Contains the actual test files that call the page objects and run tests on them using pytest.
- **`requirements.txt`:** Lists the required Python packages (Selenium, pytest, etc.) to be installed.
- **`pytest.ini`:** Configuration file for pytest. You can add specific pytest settings (e.g., command-line options) here.

---

## Example Test Execution

1. **Run all tests:**
    ```bash
    pytest
    ```

2. **Run a single test:**
    ```bash
    pytest tests/test_inputs.py
    ```

3. **Run tests with detailed output:**
    ```bash
    pytest -v
    ```

4. **Run tests in parallel (after installing `pytest-xdist`):**
    ```bash
    pytest -n auto
    ```

---

## Additional Notes

- **Browser Support:** This framework supports Chrome, Firefox, and other browsers (depending on the WebDriver configured).
- **Parallel Testing:** Use `pytest-xdist` for running tests in parallel to speed up execution.
- **Contributing:** Feel free to fork this repository and make pull requests for improvements or bug fixes.

---

Happy Testing!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.
