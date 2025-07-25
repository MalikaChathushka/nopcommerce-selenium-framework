import string
import time
import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.custom_logger import Log_Maker
from base_pages.Add_Customer_Page import Add_Customer_Page
from utilities.save_screenshot import take_screenshot
from utilities.read_properties import ReadProperties


class Test_03_Add_New_Customer:
    admin_page_url = ReadProperties.get_admin_page_url()
    username = ReadProperties.get_username()
    password = ReadProperties.get_password()
    logger = Log_Maker.log_gen()

    def test_add_new_customer(self, setup):
        self.logger.info("******** Test_03_Add_New_Customer ********")
        self.driver = setup
        self.driver.implicitly_wait(20)

        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()

        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.logger.info("******** Login Successful ********")
        time.sleep(2)

        self.add_cust = Add_Customer_Page(self.driver)
        self.add_cust.click_customer_menu()
        self.logger.info("******** Clicked on Customer Menu ********")
        time.sleep(2)

        self.add_cust.click_customers_from_menu_options()
        self.logger.info("******** Clicked on Customers from Menu Options ********")
        time.sleep(2)

        self.add_cust.click_add_new()
        self.logger.info("******** Started to provide the ********")
        time.sleep(2)

        email = generate_random_email()
        self.add_cust.enter_email(email)
        self.add_cust.enter_password("Test@123")
        self.add_cust.enter_first_name("Jack")
        self.add_cust.enter_last_name("Dawson")
        self.add_cust.select_gender("Male")
        # self.add_cust.enter_dob("01/01/1990")
        self.add_cust.enter_company_name("Test Company")
        self.add_cust.select_tax_exempt(True)
        # self.add_cust.select_newsletter("nopCommerce admin demo store")
        self.add_cust.select_customer_roles("Guests")
        self.add_cust.select_manager_of_vendor("Vendor 1")
        self.add_cust.enter_admin_comment("This is a test comment for the new customer.")
        self.add_cust.click_save()
        # self.time.sleep(3)
        self.logger.info("******** New Customer Added Successfully ********")

        customer_add_success_message = "The new customer has been added successfully."
        success_text = self.driver.find_element(By.XPATH, "//div[@class='content-wrapper']/div[1]").text

        if customer_add_success_message in success_text:
            assert True
            self.logger.info("******** Test_03_Add_New_Customer_test_passed ********")
            self.driver.close()
        else:
            self.logger.error("******** Test_03_Add_New_Customer_test_failed ********")
            take_screenshot(self.driver, "test_03_add_new_customer_failed.png")
            self.driver.close()
            assert False

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(['gmail.com', 'yahoo.com', 'example.com'])
    return f"{username}@{domain}"