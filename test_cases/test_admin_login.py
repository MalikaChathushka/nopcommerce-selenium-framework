import pytest
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Login_Admin_Page import Login_Admin_Page

class Test_01_Admin_Login:

    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"
    invalid_username = "adminrandom@yourstore.com"


    # Check the once browser open correct web page load or not
    def test_title_verification(self, setup):

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.admin_page_url)
        time.sleep(2)  # Simulate human-like delay
        actual_title = self.driver.title
        expected_title = "nopCommerce demo store. Login"

        if actual_title == expected_title:
            assert True
            self.driver.close()
        
        else:
            self.driver.close()
            assert False


    # Check the valid login happened and landing on the correct page
    def test_valid_admin_login(self, setup):

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
            assert True
            self.driver.close()
        
        else:
            self.driver.close()
            assert False
    

    # Check the invalid login happened and landing on the correct page
    def test_invalid_admin_login(self, setup):

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
            assert True
            self.driver.close()
        
        else:
            self.driver.close()
            assert False