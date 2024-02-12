# Profil Bilgileri -> Kişisel Bilgilerim Sayfası Locators
# https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim


from selenium.webdriver.common.by import By
import constants.my_personal_info_page_constants as mg

class myPersonalInfoPageLocators:
    
    first_name = (By.NAME, mg.FIRST_NAME_BYNAME)
    last_name = (By.NAME, mg.LAST_NAME_BYNAME)
    phone_number = (By.ID, mg.PHONE_NUMBER_BYID)
    birthday = (By.NAME, mg.BIRTHDAY_BYNAME)
    identification_number = (By.NAME, mg.IDENTIFICATION_NUMBER_BYNAME)
    
    country = (By.NAME, mg.COUNTRY_BYNAME)
    
    city_dropdown = (By.NAME , mg.CITY_DROPDOWN_BYNAME)
    
    district_dropdown = (By.XPATH , mg.DISTRICT_DROPDOWN_XPATH)
    district_option = (By.XPATH , mg.DISTRICT_OPTION_XPATH)
    
    address = (By.NAME, mg.ADDRESS_BYNAME)
    about = (By.CSS_SELECTOR, mg.ABOUT_CSS)
    #save_button = (By.CSS_SELECTOR , mg.SAVE_BUTTON_CSS)
    save_button = (By.XPATH, mg.SAVE_BUTTON_XPATH)

    page_toast_message = (By.CSS_SELECTOR, mg.PAGE_TOAST_MESSAGE_CSS)

    # invalid input alerts locators
    user_name_alert_message = (By.CSS_SELECTOR, mg.USERNAME_ALERT_MESSAGE_CSS )
    last_name_alert_message = (By.CSS_SELECTOR, mg.LASTNAME_ALERT_MESSAGE_CSS)
    phoneNumber_alert_message = (By.CSS_SELECTOR, mg.PHONENUMBER_ALERT_MESSAGE_CSS)
    birthday_alert_message = (By.CSS_SELECTOR, mg.BIRTHDAY_ALERT_MESSAGE_CSS)
    identificationNumber_alert_message  = (By.CSS_SELECTOR, mg.IDENTIFICATIONNUMBER_ALERT_MESSAGE_CSS) # abonelikler iç.in zorunlu alan
    invalid_identification_alert_message = (By.XPATH, mg.INVALID_IDENTIFICATON_ALERT_MESSAGE_XPATH ) # 11 haneden az/çok
    country_alert_message = (By.CSS_SELECTOR, mg.COUNTRY_ALERT_MESSAGE_CSS)
    city_alert_message = (By.CSS_SELECTOR, mg.CITY_ALERT_MESSAGE_CSS)
    district_alert_message = (By.CSS_SELECTOR, mg.DISTRICT_ALERT_MESSAGE_CSS)
    address_alert_message = (By.CSS_SELECTOR, mg.ADDRESS_ALERT_MESSAGE_CSS )
    about_alert_message = (By.CSS_SELECTOR, mg.ABOUT_ALERT_MESSAGE_CSS)
