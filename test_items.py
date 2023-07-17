import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_cart_on_page(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    assert button
