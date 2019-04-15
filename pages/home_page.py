from pages.base_page import BasePage


class HomePage(BasePage):

    def open(self):
        self.driver.get(self.__url)


    """Locators, __init__, url etc."""

    __url = "http://localhost:3000"

    def __init__(self, driver):
        super().__init__(driver)




