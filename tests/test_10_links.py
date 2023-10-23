import time
from conftest import browser
from pages.buhonline import Buhonline


def test_search_10_links(browser):
    page_element = Buhonline(browser)
    page_element.visit()
    page_element.text_placeholder.send_keys('Кассовый чек')
    # time.sleep(1)
    assert page_element.search_button.visible()
    assert page_element.search_button.exist()
    # time.sleep(1)
    page_element.search_button.click()
    # time.sleep(1)
    assert page_element.pagination_line.exist()
    time.sleep(1)



