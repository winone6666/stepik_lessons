from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    EMAIL_IMPUT_SIGN_IN = (By.CSS_SELECTOR, '#id_login-username')
    EMAIL_INPUT_SIGN_UP = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_INPUT_SIGN_UP = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_CONFIRMED_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    PASSWORD_INPUT_SIGN_IN = (By.CSS_SELECTOR, '#id_login-password')
    RESET_PASSWORD_BTN = (By.CSS_SELECTOR, '#id_login-redirect_url + p')
    SIGN_IN_BTN = (By.CSS_SELECTOR, '[name="login_submit"]')
    SIGN_UP_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ResetPasswordPageLocators():
    EMAIL_INPUT_RESET = (By.CSS_SELECTOR, '#id_email')
    SEND_PASSWORD_EMAIL_BTN = (By.CSS_SELECTOR, '.btn.btn-primary.btn-lg')
    SUCCESS_MESSAGE_SENT_EMAIL = (By.CSS_SELECTOR, '.page-header.action > h1')


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BOOK_NAME_ON_PAGE = (By.CSS_SELECTOR, 'div.product_main > h1')
    BOOK_PRICE_ON_PAGE = (By.CSS_SELECTOR, 'p.price_color')
    INFO_BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, '#messages div:nth-child(1) > div > strong')
    INFO_AMOUNT_OF_BASKET = (By.CSS_SELECTOR, '#messages div:nth-child(2) > p > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')
    WRITE_REVIEW_BTN = (By.CSS_SELECTOR, '#write_review')
    WRITE_REVIEW_LINK = (By.CSS_SELECTOR, '#reviews + p > a')


class ReviewPageLocators():
    CANCEL_REVIEW_BTN = (By.CSS_SELECTOR, '.form-group + button.btn.btn-primary.btn-lg + a')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')
    MESSAGE_INPUT = (By.CSS_SELECTOR, '#id_body')
    NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    PRODUCT_RATING = (By.CSS_SELECTOR, '.icon-star')
    SAVE_REVIEW_BTN = (By.CSS_SELECTOR, '.form-group + button.btn.btn-primary.btn-lg')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#success_message')
    TITLE_INPUT = (By.CSS_SELECTOR, '#id_title')


class ProductCatalogPageLocators():
    ADD_TO_BASKET_BTN_IN_CATALOG = (By.CSS_SELECTOR, '.btn.btn-primary.btn-block')
    HEADER_OF_PRODUCT_SEARCH_RU = (By.XPATH, '//h1[contains(., \'Товары, соответствующие запросу \')]')
    NO_PRODUCT_MESSAGE_RU = (By.XPATH, '//p[contains(., \'К сожалению, ничего не найдено.\')]')
    PRODUCT_AMOUNT_IN_CATALOG = (By.CSS_SELECTOR, '.product_pod > div > p')
    PRODUCT_IMAGE_IN_CATALOG = (By.CSS_SELECTOR, 'div.image_container > a')
    PRODUCT_NAME_IN_CATALOG = (By.CSS_SELECTOR, '.product_pod > h3 > a')
    PRODUCT_RATING_INFO_IN_CATALOG = (By.CSS_SELECTOR, '.instock.availability')
    PRODUCT_STORE_INFO_IN_CATALOG = (By.CSS_SELECTOR, '.instock.availability')


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, 'span > [href="/ru/basket/"]')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SEARCH_BTN = (By.CSS_SELECTOR, 'input[type="submit"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="search"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    APPLY_DISCOUNT_BTN = (By.CSS_SELECTOR, '#submit_discount')
    BASKET_CHECKOUT_BTN = (By.CSS_SELECTOR, 'a.btn-primary.btn-block')
    BASKET_GOOD_ITEM = (By.CSS_SELECTOR, 'div.basket-items')
    BASKET_TOTAL_INFO = (By.CSS_SELECTOR, '#basket_totals')
    BASKET_VOUCHER_INFO = (By.CSS_SELECTOR, '#voucher_form_link')
    DISCOUNT_CODE_INPUT = (By.CSS_SELECTOR, '#discount_code')
    DISCOUNT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#success_applied')
    DELETE_PRODUCT_BTN = (By.CSS_SELECTOR, 'a[data-behaviours="remove"]')
    EMPTY_BASKET_RU_TEXT = (By.XPATH, '//p[contains(., \'Ваша корзина пуста.\')]')  # language ru
