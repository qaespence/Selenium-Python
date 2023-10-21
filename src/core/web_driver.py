from selenium import webdriver


# Define a function to initialize and configure the web driver
def initialize_driver(browser="chrome"):
    if browser.lower() == "chrome":
        # Configure Chrome driver options (you can customize these options)
        chrome_options = webdriver.ChromeOptions()
        # For headless mode (no visible browser window), uncomment the next line
        # chrome_options.add_argument("--headless")
        # Specify any additional options here

        # Initialize the Chrome driver with the configured options
        driver = webdriver.Chrome(executable_path="D:\\Code\\Selenium-WDIO\\Selenium-Python\\drivers\\chromedriver.exe",
                                  options=chrome_options)
        # elif browser.lower() == "firefox":
        # Configure Firefox driver options (you can customize these options)
        firefox_options = webdriver.FirefoxOptions()
        # For headless mode (no visible browser window), uncomment the next line
        # firefox_options.add_argument("--headless")
        # Specify any additional options here

        # Initialize the Firefox driver with the configured options
        # driver = webdriver.Firefox(executable_path="path/to/geckodriver", options=firefox_options)
    else:
        raise ValueError("Unsupported browser")

    # Optionally, set a maximum timeout for page loads and element searches
    driver.implicitly_wait(10)  # Adjust the timeout value as needed

    return driver
