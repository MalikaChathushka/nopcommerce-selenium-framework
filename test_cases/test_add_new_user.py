import string  # Import string for generating random email characters
import time  # Import time for adding delays
import random  # Import random for generating random email addresses
import pytest  # Import pytest for test case structure
from selenium import webdriver  # Import webdriver for browser automation
from selenium.webdriver.common.by import By  # Import By for locating elements
from base_pages.Login_Admin_Page import Login_Admin_Page  # Import Login_Admin_Page for login actions
from utilities.custom_logger import Log_Maker  # Import Log_Maker for logging
from base_pages.Add_Customer_Page import Add_Customer_Page  # Import Add_Customer_Page for customer actions
from utilities.save_screenshot import take_screenshot  # Import take_screenshot for capturing screenshots
from utilities.read_properties import ReadProperties  # Import ReadProperties for reading config values

class Test_03_Add_New_Customer:
    admin_page_url = ReadProperties.get_admin_page_url()  # Get admin page URL from config
    username = ReadProperties.get_username()  # Get admin username from config
    password = ReadProperties.get_password()  # Get admin password from config
    logger = Log_Maker.log_gen()  # Initialize logger for logging test steps

    def test_add_new_customer(self, setup):
        self.logger.info("******** Test_03_Add_New_Customer ********")  # Log test start
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

        self.add_cust = Add_Customer_Page(self.driver)  # Create Add_Customer_Page object
        self.add_cust.click_customer_menu()  # Click on Customer menu
        self.logger.info("******** Clicked on Customer Menu ********")  # Log action
        time.sleep(2)  # Wait for menu to expand

        self.add_cust.click_customers_from_menu_options()  # Click on Customers submenu
        self.logger.info("******** Clicked on Customers from Menu Options ********")  # Log action
        time.sleep(2)  # Wait for submenu to load

        self.add_cust.click_add_new()  # Click Add New button to start adding customer
        self.logger.info("******** Started to provide the ********")  # Log action
        time.sleep(2)  # Wait for add customer form to appear

        email = generate_random_email()  # Generate a random email for the new customer
        self.add_cust.enter_email(email)  # Enter email address
        self.add_cust.enter_password("Test@123")  # Enter password for new customer
        self.add_cust.enter_first_name("Jack")  # Enter first name
        self.add_cust.enter_last_name("Dawson")  # Enter last name
        self.add_cust.select_gender("Male")  # Select gender
        # self.add_cust.enter_dob("01/01/1990")  # Optionally enter date of birth
        self.add_cust.enter_company_name("Test Company")  # Enter company name
        self.add_cust.select_tax_exempt(True)  # Select tax exempt checkbox
        # self.add_cust.select_newsletter("nopCommerce admin demo store")  # Optionally select newsletter
        self.add_cust.select_customer_roles("Guests")  # Select customer role
        self.add_cust.select_manager_of_vendor("Vendor 1")  # Select manager of vendor
        self.add_cust.enter_admin_comment("This is a test comment for the new customer.")  # Enter admin comment
        self.add_cust.click_save()  # Click save to add the new customer
        # self.time.sleep(3)  # Optionally wait after saving
        self.logger.info("******** New Customer Added Successfully ********")  # Log success

        customer_add_success_message = "The new customer has been added successfully."  # Expected success message
        success_text = self.driver.find_element(By.XPATH, "//div[@class='content-wrapper']/div[1]").text  # Get success message from page

        if customer_add_success_message in success_text:  # Check if customer was added successfully
            assert True  # Assert test passed
            self.logger.info("******** Test_03_Add_New_Customer_test_passed ********")  # Log test passed
            self.driver.close()  # Close browser
        else:
            self.logger.error("******** Test_03_Add_New_Customer_test_failed ********")  # Log test failed
            take_screenshot(self.driver, "test_03_add_new_customer_failed.png")  # Take screenshot for failure
            self.driver.close()  # Close browser
            assert False  # Assert test failed

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))  # Generate random username part
    domain = random.choice(['gmail.com', 'yahoo.com', 'example.com'])  # Randomly select domain
    return f"{username}@{domain}"  # Return the generated email