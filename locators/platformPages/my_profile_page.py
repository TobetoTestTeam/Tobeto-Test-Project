# Üst Menü , Profilim Sayfası Locators
# https://tobeto.com/profilim
#login olan kullanının profilim sayfası

# TO DO : EKLENECEK

from selenium.webdriver.common.by import By
import constants.my_profile_page_constants as mpp 

class myprofile_Locators:
    edit_button=(By.CSS_SELECTOR,mpp.EDIT_BUTTON_CSS_SELECTOR)
    my_personal_info=(By.XPATH,mpp.MY_PERSONAL_INFO_XPATH)
    eye_button=(By.CSS_SELECTOR,mpp.EYE_BUTTON_CSS_SELECTOR)
    result_page=(By.XPATH,mpp.RESULT_PAGE_XPATH)