import logging
import requests
from components.components import WebElement


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.meta_tag = WebElement(driver, 'head > meta [name=viewport]')

    def visit(self):
        return self.driver.get(self.base_url)

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        return self.get_url() == self.base_url

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False

    def code_status(self):
        resp = requests.get(self.base_url)
        return resp.status_code == 200