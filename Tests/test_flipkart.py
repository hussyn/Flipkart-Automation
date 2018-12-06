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
        '''
        Login into the application
        :return:
        '''

        numbers = self.driver.find_element(By.XPATH, Locators.number_field)
        numbers.send_keys(User_data.user_number)
        self.driver.find_element(By.XPATH, Locators.password_field).send_keys(User_data.user_password)
        self.driver.find_element(By.XPATH, Locators.submit_button).click()
        time.sleep(5)
        assert User_data.user_name_assert in self.driver.find_element(By.XPATH, Locators.text_name).text
        time.sleep(8)

    def test_select_shirt(self):
        '''
        Scenario: Category of selection from Shirts
        :return:
        '''
        self.driver.find_element(By.XPATH, Locators.cat).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Locators.selectioncat).click()
        time.sleep(6)
        assert User_data.user_selection_shirts in self.driver.find_element(By.XPATH, Locators.assertshri).text
        time.sleep(7)

    def test_sending_product(self):
        '''
        Scenario: Search a mobile device
        :return:
        '''
        self.driver.find_element(By.NAME, Locators.textfield).send_keys(User_data.user_send_keys)
        time.sleep(4)
        self.driver.find_element(By.XPATH, Locators.searchicon).click()
        time.sleep(4)
        assert User_data.user_send_keys in self.driver.find_element(By.XPATH, Locators.textarea).text
        time.sleep(6)

    def test_add_cart(self):
        self.driver.find_element(By.XPATH, Locators.cat).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.selectioncat)))
        element.click()
        time.sleep(20)
        self.driver.find_element(By.XPATH, Locators.selection_shirt).click()
        time.sleep(3)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        time.sleep(5)
        self.driver.find_element(By.ID, Locators.pin_code).send_keys("500081", Keys.ENTER)
        time.sleep(5)

        cart_sizes = self.driver.find_element(By.XPATH, Locators.cart_elements).text
        if cart_sizes == 'S':
            self.driver.find_element(By.XPATH, Locators.cart_size4).click()
            time.sleep(4)
        elif cart_sizes == 'M':
            self.driver.find_element(By.XPATH, Locators.cart_size1).click()
            time.sleep(4)
        elif cart_sizes == 'XL':
            self.driver.find_element(By.XPATH, Locators.cart_size3).click()
        else:
            self.driver.find_element(By.XPATH, Locators.cart_size2).click()
        time.sleep(6)
        self.driver.find_element(By.XPATH, Locators.cart_add_to_cart).click()
        time.sleep(3)
