import pytest  # Importing pytest for test configuration and fixtures
import undetected_chromedriver as uc  # Importing undetected_chromedriver to avoid bot detection by websites
from selenium import webdriver  # Import selenium's webdriver for Firefox and Edge
from pytest_metadata.plugin import metadata_key  # Importing metadata_key for pytest HTML reports

# This function adds a custom command-line option to pytest for selecting the browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser",                # The name of the command-line option
        action="store",             # The action to take, here it stores the value provided
        default="chrome",           # Default browser is set to Chrome
        help="Specify test browser: chrome or firefox or edge"  # Help text for the option
    )

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")  # Returns the browser option selected by the user

# This fixture sets up and tears down the WebDriver for each test
@pytest.fixture()
def setup(browser):
    # Set up the WebDriver instance based on the browser selected
    if browser == "chrome":
        driver = uc.Chrome()  # Launches a new undetected Chrome browser instance
    elif browser == "firefox":
        driver = webdriver.Firefox()  # Launches a standard Firefox browser instance
    elif browser == "edge":
        driver = webdriver.Edge()  # Launches a standard Edge browser instance
    else:
        raise ValueError("Browser not supported. Please choose chrome, firefox, or edge.") # Raise an error if an unsupported browser is specified

    yield driver          # Provides the driver to the test function
    driver.quit()         # Ensures the browser is closed after



######## for pytest html reports ########

# This function is called to configure the metadata for the pytest HTML report.
# It adds custom metadata entries like project name, module name, and tester's name.
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'nopCommerce Selenium Framework'  # Adds project name to metadata
    config.stash[metadata_key] ['Module Name'] = 'Admin Login Tests'  # Adds module name to metadata
    config.stash[metadata_key] ['Tester'] = 'Malika'  # Adds tester's name to metadata

# This function is called to modify the metadata in the HTML report
# It removes some default metadata entries that are not needed in the report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)  # Removes JAVA_HOME from metadata
    metadata.pop('Plugins', None)  # Removes Plugins from metadata