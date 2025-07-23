import pytest  # Import pytest for writing and running test cases
import time  # Import time to add delays (simulate human-like interaction)
import undetected_chromedriver as uc  # Import undetected_chromedriver to avoid bot detection
from selenium.webdriver.common.by import By  # Import By for locating elements
from selenium.webdriver.support import expected_conditions as EC  # Import EC for expected conditions
from base_pages.Login_Admin_Page import Login_Admin_Page  # Import the Login_Admin_Page page object
from utilities.read_properties import ReadProperties  # Import ReadProperties to read config values
from utilities.custom_logger import Log_Maker  # Import Log_Maker for logging test steps
from utilities.save_screenshot import take_screenshot  # Import take_screenshot utility

class Test_01_Admin_Login:

    # Read configuration values from config.ini using ReadProperties utility
    admin_page_url = ReadProperties.get_admin_page_url()  # Get admin login page URL
    username = ReadProperties.get_username()  # Get valid username
    password = ReadProperties.get_password()  # Get valid password
    invalid_username = ReadProperties.get_invalid_username()  # Get invalid username for negative test
    logger = Log_Maker.log_gen()  # Initialize logger for logging test steps

    # Test to verify the title of the login page
    def test_title_verification(self, setup):
        self.logger.info("**********Test_01_Admin_Login**********")  # Log test start
        self.logger.info("**********Test_Title_Verification**********")  # Log test step

        self.driver = setup  # Get WebDriver instance from fixture
        self.driver.maximize_window()  # Maximize browser window for better visibility
        self.driver.get(self.admin_page_url)  # Navigate to admin login page

        time.sleep(2)  # Wait for page to load (simulate human-like delay)

        actual_title = self.driver.title  # Get the current page title

        expected_title = "nopCommerce demo store. Login"  # Expected title for login page

        if actual_title == expected_title:  # Compare actual and expected titles
            take_screenshot(self.driver, "passed_test_title_verification.png")  # Take screenshot if passed
            self.logger.info("**********Title_matched**********")  # Log success
            assert True  # Assert test passed
            self.driver.close()  # Close browser
        
        else:
            take_screenshot(self.driver, "failed_test_title_verification.png")  # Take screenshot if failed
            self.logger.info("**********Title_not_matched**********")  # Log failure
            self.driver.close()  # Close browser
            assert False  # Assert test failed

    # Test to verify valid admin login
    def test_valid_admin_login(self, setup):
        self.logger.info("**********Test_02_Valid_Login**********")  # Log test start
        self.logger.info("**********Valid_Login_Verification**********")  # Log test step

        self.driver = setup  # Get WebDriver instance from fixture
        self.driver.maximize_window()  # Maximize browser window
        self.driver.get(self.admin_page_url)  # Navigate to admin login page

        time.sleep(2)  # Wait for page to load

        self.admin_lp = Login_Admin_Page(self.driver)  # Create Login_Admin_Page object with driver

        self.admin_lp.enter_username(self.username)  # Enter valid username in username field
        self.admin_lp.enter_password(self.password)  # Enter valid password in password field

        time.sleep(1)  # Wait before clicking login

        self.admin_lp.click_login()  # Click the login button

        time.sleep(3)  # Wait for dashboard to load

        actual_title = self.driver.title  # Get the current page title after login
        expected_title = "Dashboard / nopCommerce administration"  # Expected title for dashboard

        if actual_title == expected_title:  # Check if login was successful
            take_screenshot(self.driver,"passed_valid_loging_verification.png")  # Take screenshot if passed
            self.logger.info("**********Valid_login**********")  # Log success
            assert True  # Assert test passed
            self.driver.close()  # Close browser
        
        else:
            take_screenshot(self.driver,"failed_valid_loging_verification.png")  # Take screenshot if failed
            self.logger.info("**********Not_a_valid_login**********")  # Log failure
            self.driver.close()  # Close browser
            assert False  # Assert test failed

    # Test to verify invalid admin login
    def test_invalid_admin_login(self, setup):
        self.logger.info("**********Test_03_Invalid_Login**********")  # Log test start
        self.logger.info("**********Invalid_Login_Verification**********")  # Log test step

        self.driver = setup  # Get WebDriver instance from fixture
        self.driver.maximize_window()  # Maximize browser window
        self.driver.get(self.admin_page_url)  # Navigate to admin login page

        time.sleep(2)  # Wait for page to load

        self.admin_lp = Login_Admin_Page(self.driver)  # Create Login_Admin_Page object with driver

        self.admin_lp.enter_username(self.invalid_username)  # Enter invalid username
        self.admin_lp.enter_password(self.password)  # Enter valid password

        time.sleep(1)  # Wait before clicking login

        self.admin_lp.click_login()  # Click the login button

        time.sleep(3)  # Wait for error message to appear

        error_message = self.driver.find_element(By.XPATH, "//li").text  # Get error message text

        if error_message == "No customer account found":  # Check if error message is as expected
            take_screenshot(self.driver,"passed_Invalid_login_verification.png")  # Take screenshot if passed
            self.logger.info("**********Invalid_login_success**********")  # Log success
            assert True  # Assert test passed
            self.driver.close()  # Close browser
        
        else:
            take_screenshot(self.driver,"failed_invalid_loging_verification.png")  # Take screenshot if failed
            self.logger.info("**********Invalid_login_not_success**********")  # Log failure
            self.driver.close()  # Close browser
            assert False  # Assert test