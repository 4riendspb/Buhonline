import time
from conftest import browser
from pages.buhonline import Buhonline


def test_search_less_10_links(browser):
    page_element = Buhonline(browser)
    page_element.visit()
    page_element.text_placeholder.send_keys('пуск')
    time.sleep(1)
    assert page_element.search_button.visible()
    time.sleep(1)
    page_element.search_button.click()
    time.sleep(2)
    assert page_element.search_links_1.visible()
    # assert page_element.search_links_2.visible()
    # assert page_element.search_links_3.visible()
    # assert page_element.search_links_4.visible()
    # assert page_element.search_links_5.visible()
    # assert page_element.search_links_6.visible()
    # assert page_element.search_links_7.visible()
    assert not page_element.pagination_line.exist()
    time.sleep(1)