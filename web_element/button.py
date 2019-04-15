from selenium.webdriver.common.by import By

from web_element.base_element import BaseElement


class Button(BaseElement):

    def __init__(self, driver, selector):
        super().__init__(driver, selector)

    def click(self):
        super()._wait_element(self.selector)
        element = self.driver.find_element(By.XPATH, self.selector)
        element.click()
