import pytest
#from selenium.webdriver import Chrome

@pytest.fixture(scope="class")
def my_env(request):
        # global driver
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-extenstions")
        from selenium import webdriver
        driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe')
        request.cls.driver = driver
        driver.get('https://www.flipkart.com')
        driver.maximize_window()
        yield
        driver.close()
