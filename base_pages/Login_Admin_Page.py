from selenium.webdriver.common.by import By

class Login_Admin_Page:

    text_box_username_id = "Email"
    text_box_password_id = "Password"
    btn_login_xpath = "//button[normalize-space()='Log in']"

    # Creating a constructor - object for our class. driver parameter values pass by test classes
    def __init__(self, driver):
        self.driver = driver    # can access locators

    # Action method for username
    def enter_username(self, username):
        self.driver.find_element(By.ID, self.text_box_username_id).clear()
        self.driver.find_element(By.ID, self.text_box_username_id).send_keys(username)
    
    # Action method for password
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.text_box_password_id).clear()
        self.driver.find_element(By.ID, self.text_box_password_id).send_keys(password)
    
    # Action method for click the login button
    def click_login(self):
        self.driver.find_element(By.XPATH , self.btn_login_xpath).click()
