import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_Customer_Page:

    # Locators for Add Customer Page

    link_customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_menu_option_xpath = "//li[@class='nav-item']//p[normalize-space(text())='Customers']"
    link_add_new_xpath = "//div[@class='float-right']/a"
    txt_email_id = "Email"
    txt_password_id = "Password"
    txt_first_name_id = "FirstName"
    txt_last_name_id = "LastName"
    rdo_gender_male_id = "Gender_Male"
    rdo_gender_female_id = "Gender_Female"
    txt_dob_id = "DateOfBirth"
    txt_company_name_id = "Company"
    chk_is_tax_exempt_id = "IsTaxExempt"
    newsletter_cusrole_list_xpath = "//input[@class='select2-search__field']"
    cusrole_guest_xpath = "//li[contains(text(),'Guests')]"
    cusrole_administrator_xpath = "//li[contains(text(),'Administrators')]"
    cusrole_forum_moderator_xpath = "//li[contains(text(),'Forum Moderators')]"
    cusrole_registered_xpath = "//li[contains(text(),'Registered')]"
    cusrole_vendors_xpath = "//li[contains(text(),'Vendors')]"
    drpdwn_manager_of_vendor_id = "VendorId"
    txt_admin_comment_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver
    
    def click_customer_menu(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_xpath).click()
    
    def click_customers_from_menu_options(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_option_xpath).click()
    
    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.link_add_new_xpath).click()
    
    def enter_email(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)
    
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)
    
    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.txt_first_name_id).send_keys(first_name)
    
    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.txt_last_name_id).send_keys(last_name)
    
    def select_gender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdo_gender_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdo_gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.rdo_gender_female_id).click()
    
    def enter_dob(self, dob):
        self.driver.find_element(By.ID, self.txt_dob_id).send_keys(dob)
    
    def enter_company_name(self, company_name):
        self.driver.find_element(By.ID, self.txt_company_name_id).send_keys(company_name)
    
    def select_tax_exempt(self, is_tax_exempt):
        self.driver.find_element(By.ID, self.chk_is_tax_exempt_id).click()
        time.sleep(3)  # Wait for the checkbox to be processed
    
    def select_newsletter(self, value):
        newsletter_dropdown = self.driver.find_element(By.XPATH, "//li[contains(text(), 'nopCommerce admin demo store')]").click()

        # newsletter_dropdown.click()
        # time.sleep(3)  # Wait for the dropdown to be populated
        # if value == "nopCommerce admin demo store":
        #     self.driver.find_element(By.XPATH, f"//li[contains(text(), '{value}')]").click()

    
    def select_customer_roles(self, role):
        elements = self.driver.find_elements(By.XPATH, self.newsletter_cusrole_list_xpath)
        customer_roles_dropdown = elements[1]
        customer_roles_dropdown.click()

        time.sleep(3)

        if role == "Guests":
            self.driver.find_element(By.XPATH, self.cusrole_registered_xpath).click()
            time.sleep(3)
            customer_roles_dropdown.click()
            self.driver.find_element(By.XPATH, self.cusrole_guest_xpath).click()
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.cusrole_administrator_xpath).click()
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.cusrole_forum_moderator_xpath).click()
        elif role == "Registered":
            pass
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.cusrole_vendors_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.cusrole_administrator_xpath).click()
    
    def select_manager_of_vendor(self, value):
        dropdown = Select(self.driver.find_element(By.ID, self.drpdwn_manager_of_vendor_id))
        dropdown.select_by_visible_text(value)
    
    def enter_admin_comment(self, comment):
        self.driver.find_element(By.ID, self.txt_admin_comment_id).send_keys(comment)
    
    def click_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
        time.sleep(3)  # Wait for the save action to complete
        

    
