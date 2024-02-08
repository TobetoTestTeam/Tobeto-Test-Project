# Profil Bilgileri -> Medya Hesaplarım Sayfası Locators
# https://tobeto.com/profilim/profilimi-duzenle/medya-hesaplarim

from selenium.webdriver.common.by import By
import constants.my_media_accounts_page_constants as map 

class add_media_acconts_Locators:
    dropdown=(By.NAME,map.MEDIA_DROPDOWN_NAME)
    media_url=(By.NAME,map.MEDIA_URL_NAME)
    save_button=(By.XPATH,map.SAVE_BUTTON_XPATH)
    toast_body=(By.CSS_SELECTOR,map.TOAST_BODY_CSS)
    warning_message1=(By.XPATH,map.WARNING_MESSAGE1_XPATH)
    warning_message2=(By.XPATH,map.WARNING_MESSAGE2_XPATH)
    unsuccessful_toast_body=(By.XPATH,map.UNSUCCESSFUL_TOAST_BODY_XPATH)
    delete_button=(By.XPATH,map.DELETE_BUTTON_XPATH)
    delete_yes_button=(By.XPATH,map.DELETE_YES_BUTTON_XPATH)
    delete_no_button=(By.XPATH,map.DELETE_NO_BUTTON_XPATH)
    delete_toast_body=(By.XPATH,map.DELETE_TOAST_BODY_XPATH)
    media_3_message=(By.CSS_SELECTOR,map.MEDIA_3_MESSAGE_CSS)
    pencil_button=(By.XPATH,map.PENCIL_BUTTON_XPATH)
    edit_text=(By.XPATH,map.EDIT_TEXT_XPATH)
    update_button=(By.XPATH,map.UPDATE_BUTTON_XPATH)
    update_toast_body=(By.XPATH,map.DELETE_TOAST_BODY_XPATH)