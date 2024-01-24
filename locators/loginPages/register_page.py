# Kayıt Ol sayfası Locators
# https://tobeto.com/kayit-ol

from selenium.webdriver.common.by import By
import constants.register_page_constants as rg

class RegisterPageLocators:
    
    first_name = (By.NAME, rg.FIRST_NAME_BYNAME)
    last_name = (By.NAME, rg.LAST_NAME_BYNAME)
    email = (By.NAME, rg.EMAIL_BYNAME)
    password = (By.NAME, rg.PASSWORD_BYNAME)
    password_again = (By.NAME , rg.PASSWORD_AGAIN_BYNAME)
    register_button = (By.XPATH, rg.REGISTOR_BUTTON_XPATH)

    # Invalid Email
    invalid_email_alert = (By.XPATH, rg.INVALID_EMAIL_ALERT_XPATH)

    # Contract Window Locators
    contact_permission = (By.NAME, rg.CONTACT_PERMISSON_BYNAME)
    membership_contrat = (By.NAME, rg.MEMBERSHIP_CONTRACT_BYNAME)
    email_confirmation = (By.NAME, rg.EMAIL_CONFIRMATION_BYNAME)
    phone_confirmation = (By.NAME, rg.PHONE_CONFIRMATION_BYNAME)
    phone_number_country = (By.NAME, rg.PHONE_NUMBER_COUNTRY_BYNAME)
    phone_number = (By.ID, rg.PHONE_NUMBER_BYID)
    continue_button = (By.CSS_SELECTOR, rg.CONTINUE_BUTTON_BYCSS)