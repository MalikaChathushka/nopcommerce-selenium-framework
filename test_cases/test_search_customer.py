import time
import pytest
from selenium.webdriver.common.by import By
from base_pages.Search_Customer import Search_Customer_Page
from base_pages.Login_Admin_Page import Login_Admin_Page  # Import Login_Admin_Page for login actions
from utilities.custom_logger import Log_Maker  # Import Log_Maker for logging
from base_pages.Add_Customer_Page import Add_Customer_Page  # Import Add_Customer_Page for customer actions
from utilities.save_screenshot import take_screenshot  # Import take_screenshot for capturing screenshots
from utilities.read_properties import ReadProperties  # Import ReadProperties for reading config values

class Test_04_Search_Customer:
    admin_page_url = ReadProperties.get_admin_page_url()  # Get admin page URL from config
    username = ReadProperties.get_username()  # Get admin username from config
    password = ReadProperties.get_password()  # Get admin password from config
    logger = Log_Maker.log_gen()  # Initialize logger for logging test steps

    def test_search_customer_by_email(self, setup):
        self.logger.info("******** Test_04_Search_Customer ********")  # Log test start
        self.driver = setup  # Get WebDriver instance from fixture
        self.driver.implicitly_wait(20)  # Set implicit wait for element loading

        self.driver.get(self.admin_page_url)  # Navigate to admin login page
        self.driver.maximize_window()  # Maximize browser window

        self.admin_lp = Login_Admin_Page(self.driver)  # Create Login_Admin_Page object
        self.admin_lp.enter_username(self.username)  # Enter admin username
        self.admin_lp.enter_password(self.password)  # Enter admin password
        self.admin_lp.click_login()  # Click login button
        self.logger.info("******** Login Successful ********")  # Log login success
        time.sleep(2)  # Wait for login to complete

        self.logger.info("******** Navigating to Search Customer Page ********")  # Log navigation action
        self.add_cust = Add_Customer_Page(self.driver)  # Create Add_Customer_Page object
        self.add_cust.click_customer_menu()  # Click on Customer menu
        self.logger.info("******** Clicked on Customer Menu ********")
        time.sleep(2)  # Wait for menu to expand

        self.logger.info("******** Start search customer by email ********")
        self.search_customer = Search_Customer_Page(self.driver)  # Create Search_Customer_Page object
        self.search_customer.enter_customer_email("arthur_holmes@nopCommerce.com")  # Enter email to search
        self.search_customer.click_search()  # Click search button
        time.sleep(2)  # Wait for search results to load

        is_email_present = self.search_customer.search_customer_by_email("arthur_holmes@nopCommerce.com")  # Check if email is present in results
        if is_email_present == True:
            assert True, "Email found in search results"
            self.logger.info("******** Test_04_search_customer_by_email test passed ********")
            self.driver.close()  # Close the browser
        else:
            self.logger.error("******** Test_04_search_customer_by_email test failed ********")
            take_screenshot(self.driver, "test_03_add_new_customer_failed.png")  # Take screenshot for failure
            self.driver.close()
            assert False, "Email not found in search results"
    
    def test_search_customer_by_name(self, setup):
        self.logger.info("******** Test_04_Search_Customer ********")  # Log test start
        self.driver = setup  # Get WebDriver instance from fixture
        self.driver.implicitly_wait(20)  # Set implicit wait for element loading
        self.driver.get(self.admin_page_url)  # Navigate to admin login page
        self.driver.maximize_window()  # Maximize browser window

        self.admin_lp = Login_Admin_Page(self.driver)  # Create Login_Admin_Page object
        self.admin_lp.enter_username(self.username)  # Enter admin username
        self.admin_lp.enter_password(self.password)  # Enter admin password
        self.admin_lp.click_login()  # Click login button
        self.logger.info("******** Login Successful ********")  # Log login success
        time.sleep(2)  # Wait for login to complete

        self.logger.info("******** Navigating to Search Customer Page ********")  # Log navigation action
        self.add_cust = Add_Customer_Page(self.driver)  # Create Add_Customer_Page object
        self.add_cust.click_customer_menu()  # Click on Customer menu
        self.logger.info("******** Clicked on Customer Menu ********")
        time.sleep(2)  # Wait for menu to expand

        self.logger.info("******** Start search customer by name ********")
        self.search_customer = Search_Customer_Page(self.driver)  # Create Search_Customer_Page object
        self.search_customer.enter_customer_first_name("Arthur")  # Enter first name to search
        self.search_customer.enter_customer_last_name("Holmes")  # Enter last name to search
        self.search_customer.click_search()  # Click search button
        time.sleep(2)  # Wait for search results to load

        is_name_present = self.search_customer.search_customer_by_name("Arthur Holmes")  # Check if name is present in results
        if is_name_present == True:
            assert True, "Name found in search results"
            self.logger.info("******** Test_04_search_customer_by_name test passed ********")
            self.driver.close()  # Close the browser
        else:
            self.logger.error("******** Test_04_search_customer_by_name test failed ********")
            take_screenshot(self.driver, "test_04_search_customer_by_name_failed.png")  # Take screenshot for failure
            self.driver.close()
            assert False, "Name not found in search results"
    
    def test_search_customer_by_company(self, setup):
        self.logger.info("******** Test_04_Search_Customer ********")  # Log test start
        self.driver = setup  # Get WebDriver instance from fixture
        self.driver.implicitly_wait(20)  # Set implicit wait for element loading
        self.driver.get(self.admin_page_url)  # Navigate to admin login page
        self.driver.maximize_window()  # Maximize browser window
        self.admin_lp = Login_Admin_Page(self.driver)  # Create Login_Admin_Page object
        self.admin_lp.enter_username(self.username)  # Enter admin username
        self.admin_lp.enter_password(self.password)  # Enter admin password
        self.admin_lp.click_login()
        self.logger.info("******** Login Successful ********")  # Log login success
        time.sleep(2)  # Wait for login to complete

        self.logger.info("******** Navigating to Search Customer Page ********")  # Log navigation action
        self.add_cust = Add_Customer_Page(self.driver)  # Create Add_Customer_Page object
        self.add_cust.click_customer_menu()  # Click on Customer menu
        self.logger.info("******** Clicked on Customer Menu ********")
        time.sleep(2)  # Wait for menu to expand

        self.logger.info("******** Start search customer by company ********")
        self.search_customer = Search_Customer_Page(self.driver)  # Create Search_Customer_Page object
        self.search_customer.enter_customer_company("Test Company")  # Enter company name to search
        self.search_customer.click_search()  # Click search button
        time.sleep(2)  # Wait for search results to load

        is_company_present = self.search_customer.search_customer_by_name("Test Company")  # Check if company is present in results
        if is_company_present == True:
            assert True, "Company found in search results"
            self.logger.info("******** Test_04_search_customer_by_company test passed ********")
            self.driver.close()  # Close the browser
        else:
            self.logger.error("******** Test_04_search_customer_by_company test failed ********")
            take_screenshot(self.driver, "test_04_search_customer_by_company_failed.png")  # Take screenshot for failure
            self.driver.close()
            assert False, "Company not found in search results"
