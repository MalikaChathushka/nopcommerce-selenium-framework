from selenium.webdriver.common.by import By  # Import By class to locate elements in Selenium

class Login_Admin_Page:
    # create and store the locators
    text_box_username_id = "Email"  # Locator for the username input field (by ID)
    text_box_password_id = "Password"  # Locator for the password input field (by ID)
    btn_login_xpath = "//button[normalize-space()='Log in']"  # Locator for the login button (by XPath)
    btn_logout_linktext = "Logout"  # Locator for the logout button (by XPath)

    # Creating a constructor - object for our class. driver parameter values pass by test classes
    def __init__(self, driver):
        self.driver = driver    # Store the WebDriver instance for use in page methods

    # Action method for username
    def enter_username(self, username):
        self.driver.find_element(By.ID, self.text_box_username_id).clear()  # Clear any existing text in the username field
        self.driver.find_element(By.ID, self.text_box_username_id).send_keys(username)  # Enter the provided username

    # Action method for password
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.text_box_password_id).clear()  # Clear any existing text in the password field
        self.driver.find_element(By.ID, self.text_box_password_id).send_keys(password)  # Enter the provided password

    # Action method for click the login button
    def click_login(self):
        self.driver.find_element(By.XPATH , self.btn_login_xpath).click()  # Click the login button to submit

    # Action method for click the logout button
    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.btn_logout_linktext).click() # Click the logout button to log out of the admin panel