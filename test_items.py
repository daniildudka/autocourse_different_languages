import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_the_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    add_button = len(browser.find_elements(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]'))
    assert add_button > 0, "No button on the page"