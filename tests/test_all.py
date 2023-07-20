from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.chromium.options import ChromiumOptions
import allure
import pytest

@pytest.fixture
def driver():
    options = ChromiumOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(1)
    return driver


@allure.severity(allure.severity_level.NORMAL)
class TestSelenium:

    @allure.severity(allure.severity_level.MINOR)
    def test_check_working(self, driver):
        driver.get('https://www.selenium.dev/')
        status = driver.find_element(By.XPATH, '//*[local-name()="svg" and @id="selenium_webdriver"]').is_displayed()
        
        if status: assert True
        else: assert False

        driver.close()
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_another(self):
        pytest.skip('This test will be implemented later...')

    @allure.severity(allure.severity_level.CRITICAL)    
    def test_goto_webdriver_page(self, driver):
        driver.get('https://www.selenium.dev/')
        link =driver.find_element(By.XPATH,'//a[contains(@class, "webdriver")]').get_attribute('href')
        driver.get(link)
        status = driver.find_element(By.XPATH,'//h1[text()="WebDriver"]').is_displayed()
        
        if status: 
            allure.attach(driver.get_screenshot_as_png(), name='webdriverPageScreen', attachment_type=AttachmentType.PNG) 
            assert True
        else:
            allure.attach(driver.get_screenshot_as_png(), name='webdriverPageScreen', attachment_type=AttachmentType.PNG) 
            assert False
        
        driver.close()