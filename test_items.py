import time


def test_button_add_to_basket_is_exist(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/hackers-painters_185/")
    time.sleep(30)
    assert browser.find_element_by_class_name(
        "btn-add-to-basket"
    ).is_displayed(), "Button add to basket is not exist"

