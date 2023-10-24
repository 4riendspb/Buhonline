import time
from conftest import browser
from pages.buhonline import Buhonline


def test_element(browser):
    search_menu = Buhonline(browser)
    search_menu.visit()

    assert search_menu.search_menu.visible()
    assert search_menu.search_menu.exist()

    assert search_menu.search_loop.visible()
    assert search_menu.search_loop.exist()

    assert search_menu.search_loop.check_css('width', '16px')