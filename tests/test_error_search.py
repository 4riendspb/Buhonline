import time
from conftest import browser
from pages.buhonline import Buhonline


def test_search_less_10_links(browser):
    page_element = Buhonline(browser)
    page_element.visit()
    page_element.text_placeholder.send_keys('akhfjjhvcb,k')
    assert page_element.search_button.visible()
    page_element.search_button.click()
    assert page_element.error_icon.exist()
    assert page_element.error_icon.visible()
    assert page_element.error_icon.check_css('width', '64px')
    assert page_element.error_text_1.visible()
    assert page_element.error_text_1.exist()
    assert page_element.error_text_2.visible()
    assert page_element.error_text_2.exist()

    time.sleep(1)
