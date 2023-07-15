from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import allure
import pytest

@allure.severity(allure.severity_level.NORMAL)
class TestSelenium:

    @allure.severity(allure.severity_level.MINOR)
    def test_check_working(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.driver.get('https://www.selenium.dev/')
        status = self.driver.find_element(By.XPATH, '//*[local-name()="svg" and @id="selenium_webdriver"]').is_displayed()
        
        if status: assert True
        else: assert False

        self.driver.close()
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_another(self):
        pytest.skip('This test will be implemented later...')

    @allure.severity(allure.severity_level.CRITICAL)    
    def test_goto_webdriver_page(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.driver.get('https://www.selenium.dev/')
        link =self.driver.find_element(By.XPATH,'//a[contains(@class, "webdriver")]').get_attribute('href')
        self.driver.get(link)
        status = self.driver.find_element(By.XPATH,'//h1[text()="WebDriver"]').is_displayed()
        
        if status: 
            allure.attach(self.driver.get_screenshot_as_png(), name='webdriverPageScreen', attachment_type=AttachmentType.PNG) 
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='webdriverPageScreen', attachment_type=AttachmentType.PNG) 
            assert False
        
        self.driver.close()