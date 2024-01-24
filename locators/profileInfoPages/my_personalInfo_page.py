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
    #save_button = (By.CSS_SELECTOR , mg.SAVE_BUTTON_CSS)
    save_button = (By.XPATH, mg.SAVE_BUTTON_XPATH)
