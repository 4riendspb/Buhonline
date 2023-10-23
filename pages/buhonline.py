from components.components import WebElement
from pages.base_page import BasePage


class Buhonline(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.buhonline.ru/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '')
        self.btn_elements = WebElement(driver, '')
        self.footer_text = WebElement(driver, '')
        self.h5 = WebElement(driver, '')
