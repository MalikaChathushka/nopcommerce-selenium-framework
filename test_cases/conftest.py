import pytest
import undetected_chromedriver as uc

@pytest.fixture()
def setup():
    driver = uc.Chrome()
    yield driver
    driver.quit()