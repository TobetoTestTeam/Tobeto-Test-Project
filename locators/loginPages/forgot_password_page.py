# Şifremi Unuttum Sayfası Locators
# https://tobeto.com/sifremi-unuttum

from selenium.webdriver.common.by import By
import constants.forgot_password_constants as fc

class forgotPasswordPageLocators:

    forgot_password_textbox = (By.CSS_SELECTOR, fc.FORGOT_PASSWORD_TEXTBOX_CSS)
    submit_button = (By.CSS_SELECTOR, fc.SUBMIT_BUTTON_CSS)
    warning_message_field = (By.CSS_SELECTOR, fc.WARNING_MESSAGE_CSS)
