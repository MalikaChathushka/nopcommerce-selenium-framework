import time  # Import time module to add delays where needed

from selenium.webdriver.common.by import By  # Import By for locating elements
from selenium.webdriver.support.select import Select  # Import Select for handling dropdowns

class Add_Customer_Page:

    # Locators for Add Customer Page (used to find elements on the page)
    link_customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"  # Locator for Customers menu
    link_customer_menu_option_xpath = "//li[@class='nav-item']//p[normalize-space(text())='Customers']"  # Locator for Customers submenu option
    link_add_new_xpath = "//div[@class='float-right']/a"  # Locator for Add New button
    txt_email_id = "Email"  # Locator for Email input field
    txt_password_id = "Password"  # Locator for Password input field
    txt_first_name_id = "FirstName"  # Locator for First Name input field
    txt_last_name_id = "LastName"  # Locator for Last Name input field
    rdo_gender_male_id = "Gender_Male"  # Locator for Male gender radio button
    rdo_gender_female_id = "Gender_Female"  # Locator for Female gender radio button
    txt_dob_id = "DateOfBirth"  # Locator for Date of Birth input field
    txt_company_name_id = "Company"  # Locator for Company Name input field
    chk_is_tax_exempt_id = "IsTaxExempt"  # Locator for Tax Exempt checkbox
    newsletter_cusrole_list_xpath = "//input[@class='select2-search__field']"  # Locator for select2 dropdown search fields
    cusrole_guest_xpath = "//li[contains(text(),'Guests')]"  # Locator for Guests role
    cusrole_administrator_xpath = "//li[contains(text(),'Administrators')]"  # Locator for Administrators role
    cusrole_forum_moderator_xpath = "//li[contains(text(),'Forum Moderators')]"  # Locator for Forum Moderators role
    cusrole_registered_xpath = "//li[contains(text(),'Registered')]"  # Locator for Registered role
    cusrole_vendors_xpath = "//li[contains(text(),'Vendors')]"  # Locator for Vendors role
    drpdwn_manager_of_vendor_id = "VendorId"  # Locator for Manager of Vendor dropdown
    txt_admin_comment_id = "AdminComment"  # Locator for Admin Comment input field
    btn_save_xpath = "//button[@name='save']"  # Locator for Save button

    def __init__(self, driver):
        self.driver = driver  # Store the WebDriver instance for use in page methods

    def click_customer_menu(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_xpath).click()  # Click the Customers menu

    def click_customers_from_menu_options(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_option_xpath).click()  # Click the Customers submenu option

    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.link_add_new_xpath).click()  # Click the Add New button

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)  # Enter the email address

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)  # Enter the password

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.txt_first_name_id).send_keys(first_name)  # Enter the first name

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.txt_last_name_id).send_keys(last_name)  # Enter the last name

    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdo_gender_male_id).click()  # Select Male gender
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdo_gender_female_id).click()  # Select Female gender
        else:
            self.driver.find_element(By.ID, self.rdo_gender_female_id).click()  # Default to Female if not specified

    def enter_dob(self, dob):
        self.driver.find_element(By.ID, self.txt_dob_id).send_keys(dob)  # Enter the date of birth

    def enter_company_name(self, company_name):
        self.driver.find_element(By.ID, self.txt_company_name_id).send_keys(company_name)  # Enter the company name

    def select_tax_exempt(self, is_tax_exempt):
        self.driver.find_element(By.ID, self.chk_is_tax_exempt_id).click()  # Click the Tax Exempt checkbox
        time.sleep(3)  # Wait for the checkbox to be processed

    def select_newsletter(self, value):
        # Find all select2 search fields (newsletter and customer roles dropdowns)
        elements = self.driver.find_elements(By.XPATH, self.newsletter_cusrole_list_xpath)  # Get all select2 dropdown search fields
        newsletter_dropdown = elements[0]  # The first element is usually the newsletter dropdown
        newsletter_dropdown.click()  # Click to open the newsletter dropdown
        time.sleep(2)  # Wait for the dropdown to be populated
        self.driver.find_element(By.XPATH, f"//li[contains(text(), '{value}')]").click()  # Select the newsletter by visible text

    def select_customer_roles(self, role):
        elements = self.driver.find_elements(By.XPATH, self.newsletter_cusrole_list_xpath)  # Get all select2 dropdown search fields
        customer_roles_dropdown = elements[1]  # The second element is usually the customer roles dropdown
        customer_roles_dropdown.click()  # Click to open the customer roles dropdown

        time.sleep(3)  # Wait for dropdown options to load

        if role == "Guests":
            self.driver.find_element(By.XPATH, self.cusrole_registered_xpath).click()  # Remove Registered role first
            time.sleep(3)  # Wait for UI update
            customer_roles_dropdown.click()  # Reopen dropdown
            self.driver.find_element(By.XPATH, self.cusrole_guest_xpath).click()  # Select Guests role
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.cusrole_administrator_xpath).click()  # Select Administrators role
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.cusrole_forum_moderator_xpath).click()  # Select Forum Moderators role
        elif role == "Registered":
            pass  # Do nothing if Registered role is needed
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.cusrole_vendors_xpath).click()  # Select Vendors role
        else:
            self.driver.find_element(By.XPATH, self.cusrole_administrator_xpath).click()  # Default to Administrators role

    def select_manager_of_vendor(self, value):
        dropdown = Select(self.driver.find_element(By.ID, self.drpdwn_manager_of_vendor_id))  # Find the Manager of Vendor dropdown
        dropdown.select_by_visible_text(value)  # Select the vendor manager by visible text

    def enter_admin_comment(self, comment):
        self.driver.find_element(By.ID, self.txt_admin_comment_id).send_keys(comment)  # Enter the admin comment

    def click_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()  # Click the Save button to submit the form
        time.sleep(3)  # Wait for the save