from selenium.webdriver.common.by import By

class Search_Customer_Page:

    text_email_id = "SearchEmail"
    text_first_name_id = "SearchFirstName"
    text_last_name_id = "SearchLastName"
    btn_search_id = "search-customers"
    text_company_id = "SearchCompany"

    rows_table_xpath = "//table[@id='customers-grid']/tbody//tr"
    columns_table_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver
    
    def enter_customer_email(self, email):
        self.driver.find_element(By.ID, self.text_email_id).clear()
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)
    
    def enter_customer_first_name(self, first_name):
        self.driver.find_element(By.ID, self.text_first_name_id).clear()
        self.driver.find_element(By.ID, self.text_first_name_id).send_keys(first_name)
    
    def enter_customer_last_name(self, last_name):
        self.driver.find_element(By.ID, self.text_last_name_id).clear()
        self.driver.find_element(By.ID, self.text_last_name_id).send_keys(last_name)
    
    def enter_customer_company(self, company):
        self.driver.find_element(By.ID, self.text_company_id).clear()
        self.driver.find_element(By.ID, self.text_company_id).send_keys(company)
    
    def click_search(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()
    
    def get_results_table_rows(self):
        return self.driver.find_elements(By.XPATH, self.rows_table_xpath)

    def get_results_table_columns(self):
        return self.driver.find_elements(By.XPATH, self.columns_table_xpath)
    
    def search_customer_by_email(self, email):
        email_present_flag = False

        for r in range(1, len(self.get_results_table_rows()) + 1):
            cus_email = self.driver.find_element(By.XPATH, "//table[@id='customer-grid']/tbody//tr["+str(r)+"]/td[2]").text
            
            if cus_email == email:
                email_present_flag = True
                break
        return email_present_flag
    
    def search_customer_by_name(self, name):
        name_present_flag = False

        for r in range(1, self.get_results_table_rows() + 1):
            cus_name = self.driver.find_element(By.XPATH, "//table[@id='customer-grid']/tbody//tr["+str(r)+"]/td[3]").text
            
            if cus_name == name:
                name_present_flag = True
                break
        return name_present_flag
    
    def search_customer_by_company(self, company):
        company_present_flag = False

        for r in range(1, self.get_results_table_rows() + 1):
            cus_company = self.driver.find_element(By.XPATH, "//table[@id='customer-grid']/tbody//tr["+str(r)+"]/td[5]").text
            
            if cus_company == company:
                company_present_flag = True
                break
        return company_present_flag