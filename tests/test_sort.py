import time
from conftest import browser
from pages.buhonline import Buhonline


def test_sort(browser):
    page_element = Buhonline(browser)
    page_element.visit()
    page_element.text_placeholder.send_keys('Кассовый чек')
    # time.sleep(1)

    assert page_element.search_button.visible()
    assert page_element.search_button.exist()

    page_element.search_button.click()
    assert page_element.pagination_line.exist()
    time.sleep(1)

    assert page_element.filter_btn.exist()
    page_element.filter_btn.click()
    # time.sleep(1)
    page_element.select_filter_btn.click()
    page_element.refresh()
    page_element.filter_btn.click()
    page_element.select_filter_btn_next.click()

    # assert len(page_element.window_handles) == 1
    page_element.new_tab.click()
    time.sleep(2)

    time.sleep(2)
