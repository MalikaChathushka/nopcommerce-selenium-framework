import pytest
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import ReadProperties
from utilities.custom_logger import Log_Maker
from utilities.save_screenshot import take_screenshot


class Test_01_Admin_Login:

    # Initialize the Read_Config class to access configuration properties
    # Read the url, username, password and invalid username from config.ini file
    admin_page_url = ReadProperties.get_admin_page_url()
    username = ReadProperties.get_username()
    password = ReadProperties.get_password()
    invalid_username = ReadProperties.get_invalid_username()
    logger = Log_Maker.log_gen()

    # Check the once browser open correct web page load or not
    def test_title_verification(self, setup):
        self.logger.info("**********Test_01_Admin_Login**********")
        self.logger.info("**********Test_Title_Verification**********")

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.admin_page_url)

        time.sleep(2)  # Simulate human-like delay

        actual_title = self.driver.title

        expected_title = "nopCommerce demo store. Login"

        if actual_title == expected_title:
            self.logger.info("**********Title_matched**********")
            assert True
            self.driver.close()
        
        else:
            # self.driver.take_screenshot("test_title_verification.png")
            self.logger.info("**********Title_not_matched**********")
            self.driver.close()
            assert False


    # Check the valid login happened and landing on the correct page
    def test_valid_admin_login(self, setup):
        self.logger.info("**********Test_02_Valid_Login**********")
        self.logger.info("**********Valid_Login_Verification**********")

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.admin_page_url)

        time.sleep(2)  # Simulate human-like delay

        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)

        time.sleep(1)

        self.admin_lp.click_login()

        time.sleep(3)

        actual_title = self.driver.title
        expected_title = "Dashboard / nopCommerce administration"

        if actual_title == expected_title:
            self.logger.info("**********Valid_login**********")
            assert True
            self.driver.close()
        
        else:
            self.logger.info("**********Not_a_valid_login**********")
            self.driver.close()
            assert False
    

    # Check the invalid login happened and landing on the correct page
    def test_invalid_admin_login(self, setup):
        self.logger.info("**********Test_03_Invalid_Login**********")
        self.logger.info("**********Invalid_Login_Verification**********")

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.admin_page_url)

        time.sleep(2)  # Simulate human-like delay

        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)

        time.sleep(1)

        self.admin_lp.click_login()

        time.sleep(3)

        error_message = self.driver.find_element(By.XPATH, "//li").text

        if error_message == "No customer account found":
            self.logger.info("**********Invalid_login_success**********")
            assert True
            self.driver.close()
        
        else:
            self.logger.info("**********Invalid_login_not_success**********")
            self.driver.close()
            assert False