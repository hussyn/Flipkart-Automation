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
        time.sleep(8)

    def test_select_test(self):
        self.driver.find_element(By.XPATH, Locators.cat).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Locators.selectioncat).click()
        time.sleep(6)
        assert User_data.user_selection_shirts in self.driver.find_element(By.XPATH, Locators.assertshri).text
        time.sleep(7)

    def test_sending_product(self):
        self.driver.find_element(By.NAME, Locators.textfield).send_keys(User_data.user_send_keys)
        time.sleep(4)
        self.driver.find_element(By.XPATH, Locators.searchicon).click()
        time.sleep(4)
        assert User_data.user_send_keys in self.driver.find_element(By.XPATH, Locators.textarea).text
        time.sleep(6)

    def test_add_product(self):
        self.driver.find_element(By.XPATH, Locators.selct).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.productselected)))
        element.click()
        time.sleep(20)
        self.driver.find_element(By.XPATH, Locators.subproduct).click()
        time.sleep(3)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        time.sleep(5)
        self.driver.find_element(By.ID, Locators.pin_code).send_keys("500081", Keys.ENTER)
        time.sleep(5)
        try:
            elem = self.driver.find_element(By.XPATH, Locators.click_btm).click()
            if elem.is_displayed():
                elem.click()
                time.sleep(6)

        except:
            print("No Such Element found!")



