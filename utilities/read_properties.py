import configparser

config = configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')

class ReadProperties:
    @staticmethod
    def get_admin_page_url():
        url =  config.get('admin login information', 'admin_page_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('admin login information', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login information', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('admin login information', 'invalid_username')
        return invalid_username