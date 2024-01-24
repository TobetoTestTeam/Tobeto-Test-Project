
# Login Sayfası Locators
# https://tobeto.com/giris

from selenium.webdriver.common.by import By
import constants.login_page_constants as lg

class LoginPageLocators:
    
    user_email = (By.XPATH, lg.USER_EMAIL_XPATH)
    user_password = (By.XPATH, lg.USER_PASSWORD_XPATH)
    giris_button = (By.XPATH, lg.GIRIS_BUTTON_XPATH)
    warning_field_mail = (By.XPATH, lg.WARNING_FIELD_MAIL)
    warning_field_pass = (By.CSS_SELECTOR , lg.WARNING_FIELD_PASS)