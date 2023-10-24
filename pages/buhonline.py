from components.components import WebElement
from pages.base_page import BasePage


class Buhonline(BasePage):

    def __init__(self, driver):

        self.base_url = 'https://www.buhonline.ru/'
        super().__init__(driver, self.base_url)

        self.text_placeholder = WebElement(driver, 'div.searchWrap--57d3.searchWrap_bgr--4062.hidden-xs.noprint > div '
                                                   '> div > div > form > div.input_bo_wrap--1b7e > input')
        self.search_button = WebElement(driver, '#header-react-app > div.searchWrap--57d3.searchWrap_bgr--4062.hidden'
                                                '-xs.noprint > div > div > div > form > button')
        self.pagination_line = WebElement(driver, 'div.veil-block > div')

        self.search_links_1 = WebElement(driver, '#site-search-result-react-app > div > div:nth-child(1)')
        # self.search_links_2 = WebElement(driver, '#site-search-result-react-app > div > div:nth-child(2)')
        # self.search_links_3 = WebElement(driver, '#site-search-result-react-app > div > div:nth-child(3)')
        # self.search_links_4 = WebElement(driver, '#site-search-result-react-app > div > div:nth-child(4)')
        # self.search_links_5 = WebElement(driver, '#site-search-result-react-app > div > div:nth-child(5)')
        # self.search_links_6 = WebElement(driver, '#site-search-result-react-app > div > div:nth-child(6)')
        # self.search_links_7 = WebElement(driver, '#site-search-result-react-app > div > div:nth-child(7)')
        self.error_icon = WebElement(driver, '#site-search-result-react-app > div > div > '
                                             'div.errorMessageIcon--a2c4.errorMessageIcon_empty--95a6')
        self.error_text_1 = WebElement(driver,'div.errorMessageTitle--767f')
        self.error_text_2 = WebElement(driver,'div > p')

        self.filter_btn = WebElement(driver, 'div.filters--eaa2 > span')
        self.select_filter_btn = WebElement(driver,'div.searchOptions--df0c > div.filters--eaa2 > nav > li:nth-child('
                                                   '2) > a')
        self.select_filter_btn_next = WebElement(driver, 'div.filters--eaa2 > nav > li:nth-child(2) > a')

        self.new_tab = WebElement(driver, 'div.titleWrap--173e')
        self.new_tub = WebElement(driver, 'div.titleWrap--173e')

        self.search_menu = WebElement(driver, '.searchWrap_bgr--4062.hidden-xs.noprint > div > div > div > form > '
                                              'div.input_bo_wrap--1b7e')
        self.search_loop = WebElement(driver, '#header-react-app > div.searchWrap--57d3.searchWrap_bgr--4062.hidden'
                                              '-xs.noprint > div > div > div > form > div.searchIcon--6d32 > svg')










