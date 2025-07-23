import configparser  # Import configparser to read configuration files

config = configparser.RawConfigParser()  # Create a RawConfigParser object to handle config file parsing
config.read('.\\configurations\\config.ini')  # Read the config.ini file from the configurations directory

class ReadProperties:
    @staticmethod
    def get_admin_page_url():
        url =  config.get('admin login information', 'admin_page_url')  # Get the admin page URL from the config file
        return url  # Return the admin page URL

    @staticmethod
    def get_username():
        username = config.get('admin login information', 'username')  # Get the username from the config file
        return username  # Return the username

    @staticmethod
    def get_password():
        password = config.get('admin login information', 'password')  # Get the password from the config file
        return password  # Return the password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('admin login information', 'invalid_username')  # Get the invalid username for negative test cases
        return invalid_username  # Return the