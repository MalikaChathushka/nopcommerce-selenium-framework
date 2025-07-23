import pytest  # Import pytest for writing and running test cases
import time  # Import time to add delays (simulate human-like interaction)
import undetected_chromedriver as uc  # Import undetected_chromedriver to avoid bot detection
from selenium.webdriver.common.by import By  # Import By for locating elements
from selenium.webdriver.support import expected_conditions as EC  # Import EC for expected conditions
from base_pages.Login_Admin_Page import Login_Admin_Page  # Import the Login_Admin_Page page object
from utilities.read_properties import ReadProperties  # Import ReadProperties to read config values
from utilities.custom_logger import Log_Maker  # Import Log_Maker for logging test steps
from utilities.save_screenshot import take_screenshot  # Import take_screenshot utility
from utilities.excel_utils import get_row_count, get_column_count, read_data  # Import Excel utilities for data-driven tests

class Test_02_Data_Driven_Admin_Login:

    # Read configuration values from config.ini using ReadProperties utility
    admin_page_url = ReadProperties.get_admin_page_url()  # Get admin login page URL
    logger = Log_Maker.log_gen()  # Initialize logger for logging test steps
    path = ".//test_data//admin_login_data.xlsx"  # Path to the Excel file containing test data
    status_list = []  # Initialize a list to store test results
    

    # Test to verify valid admin login
    def test_valid_admin_login_data_driven(self, setup):
        self.logger.info("**********Test_02_Valid_Login**********")  # Log test start
        self.logger.info("**********Valid_Login_Verification**********")  # Log test step

        self.driver = setup  # Get WebDriver instance from fixture
        self.driver.implicitly_wait(10)  # Set implicit wait for elements to load
        self.driver.maximize_window()  # Maximize browser window
        self.driver.get(self.admin_page_url)  # Navigate to admin login page

        time.sleep(2)  # Wait for page to load

        self.admin_lp = Login_Admin_Page(self.driver)  # Create Login_Admin_Page object with driver

        self.row_count = get_row_count(".//test_data//admin_login_data.xlsx", "Sheet1")  # Get total number of rows in the sheet
        
        for row in range(2, self.row_count + 1):  # Loop through each row starting from the second row
            self.username = read_data(self.path, "Sheet1", row, 1)  # Read username from the Excel file
            self.password = read_data(self.path, "Sheet1", row, 2)  # Read password from the Excel file
            self.exp_login = read_data(self.path, "Sheet1", row, 3)  # Read expected login result from the Excel file
            self.admin_lp.enter_username(self.username)  # Enter valid username in username field
            self.admin_lp.enter_password(self.password)  # Enter valid password in password field

            time.sleep(1)  # Wait before clicking login

            self.admin_lp.click_login()  # Click the login button

            time.sleep(3)  # Wait for dashboard to load

            actual_title = self.driver.title  # Get the current page title after login
            expected_title = "Dashboard / nopCommerce administration"  # Expected title for dashboard

            if actual_title == expected_title:
                if self.exp_login == "Yes":  # Check if login was successful
                    take_screenshot(self.driver, f"passed_valid_login_row_{row}.png")  # Take screenshot if passed
                    self.logger.info(f"**********Valid_login_row_{row}**********")  # Log success
                    self.status_list.append("Pass")
                    self.admin_lp.click_logout()  # Click logout after successful login
                    time.sleep(2)  # Wait for logout to complete
                    
                elif self.exp_login == "No":
                    take_screenshot(self.driver, f"failed_valid_login_row_{row}.png")  # Take screenshot if failed
                    self.logger.info(f"**********Not_a_valid_login_row_{row}**********")  # Log failure
                    self.status_list.append("Fail")
                    self.admin_lp.click_logout()  # Click logout after failed login
                    time.sleep(2)  # Wait for logout to complete
                    
            elif actual_title != expected_title:
                if self.exp_login == "Yes":
                    take_screenshot(self.driver, f"failed_valid_login_row_{row}.png")  # Take screenshot if failed
                    self.logger.info(f"**********Not_a_valid_login_row_{row}**********")  # Log failure
                    self.status_list.append("Fail")
                    
                elif self.exp_login == "No":
                    take_screenshot(self.driver, f"passed_valid_login_row_{row}.png")   # Take screenshot if passed
                    self.logger.info(f"**********Valid_login_row_{row}**********")  # Log success
                    self.status_list.append("Pass")
                    

        print("Test Results:", self.status_list)  # Print the results of all test cases

        if "Fail" in self.status_list:
            self.logger.info("**********Some tests failed**********")  # Log if any test failed
            assert False  # Assert test failed if any case failed
        else:
            self.logger.info("**********All tests passed**********")
            assert True  # Assert test passed if all cases passed