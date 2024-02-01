# Profil Bilgileri -> Deneyeimlerim Sayfası Locators
# https://tobeto.com/profilim/profilimi-duzenle/deneyimlerim

from selenium.webdriver.common.by import By
import constants.my_experiences_page_constants as mg

class myExperiencesPageLocators:
    
    CORPORATION_NAME = (By.XPATH, mg.CORPORATION_NAME_XPATH)
    POSITION = (By.XPATH, mg.POSITION_XPATH)
    SECTOR = (By.XPATH, mg.SECTOR_XPATH)
    SELECT_COUNTRY_DROPDOWN = (By.XPATH, mg.SELECT_COUNTRY_DROPDOWN_XPATH)
    START_CALENDAR = (By.XPATH, mg.START_CALENDAR_XPATH)
    START_DATE = (By.CSS_SELECTOR, mg.START_DATE_CSS)
    FINISH_CALENDAR = (By.XPATH, mg.FINISH_CALENDAR_XPATH)
    FINISH_DATE =(By.CSS_SELECTOR, mg.FINISH_DATE_CSS)
    SAVE_BUTTON = (By.CSS_SELECTOR, mg.SAVE_BUTTON_XPATH)

    TOAST_MESSAGE = (By.CSS_SELECTOR, mg.TOAST_MESSAGE_CSS)