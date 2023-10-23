import logging
import requests
from components.components import WebElement

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.meta_tag = WebElement(driver, 'head > meta [name=viewport]')