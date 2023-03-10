from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_PASSWORD_REPEAT = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button.btn[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    BASKET_SUM_PRICE = (By.XPATH, "//div[@id='messages']/child::*[position()=3]//p/strong")
    BASKET_SUM_PRICE_MESSAGE = (By.XPATH, "//div[@id='messages']/child::*[position()=3]")
    PRODUCT_ADDED_TO_BASKET_MESSAGE = (By.XPATH, "//div[@id='messages']/child::*[position()=1]//strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/child::*[position()=1]")


class BasePageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "div#content_inner p")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
