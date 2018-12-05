from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


from POM.Locators import Locators
from POM.User_Data import User_data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
import conftest

@pytest.mark.usefixtures("my_env")


class BaseTest:
    pass


class Testing(BaseTest):

    def test_login(self):

        numbers = self.driver.find_element(By.XPATH, Locators.number_field)
        numbers.send_keys(User_data.user_number)
        self.driver.find_element(By.XPATH, Locators.password_field).send_keys(User_data.user_password)
        self.driver.find_element(By.XPATH, Locators.submit_button).click()
        time.sleep(5)
        assert User_data.user_name_assert in self.driver.find_element(By.XPATH, Locators.text_name).text