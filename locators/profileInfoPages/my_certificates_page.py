# Profil Bilgileri -> Sertifikalarım Sayfası Locators
# https://tobeto.com/profilim/profilimi-duzenle/sertifikalarim

from selenium.webdriver.common.by import By
import constants.my_certificates_page_constants as cpc

class delete_certificate_Locators:

    dustbin_button = (By.XPATH, cpc.DUSTBIN_BUTTON_XPATH)
    yes_button = (By.XPATH, cpc.YES_BUTTON_XPATH)
    information_popup = (By.XPATH, cpc.INFORMATION_POPUP_XPATH)