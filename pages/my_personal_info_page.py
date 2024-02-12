# Profil Bilgileri -> Kişisel Bilgilerim Sayfası 
# https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.profileInfoPages.my_personalInfo_page import myPersonalInfoPageLocators as mg_locate

class MyPersonalInfoPage: 

    def __init__(self):
        self.driver = webdriver.Chrome()
        
        #self.driver.get("https://tobeto.com/giris")
        #self.driver.maximize_window()
    
    def gotoPage(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()

    
    def get_firstname_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.first_name))
    
    def get_lastname_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.last_name))
    
    def get_phoneNumber_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.phone_number))
    
    def get_birthday_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.birthday))
    
    def get_identificationNumber_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.identification_number))
    
    def get_country_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.country))
    
    def get_cityDropdown_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.city_dropdown))
    
    def get_districtDropdown_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.district_dropdown))
    
    def get_address_element(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(mg_locate.address))
    
    def get_about_element(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(mg_locate.about))

    def get_saveButton_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.save_button))
    
    def get_pageToastMessage_element(self):
        return WebDriverWait(self.driver, 50).until(ec.presence_of_element_located(mg_locate.page_toast_message))

    # invalid input alerts elements
    def get_userNameAlertMessage_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.user_name_alert_message))
    
    def get_lastnameAlertMessage_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.last_name_alert_message))

    def get_phoneNumberAlertMessage_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.phoneNumber_alert_message))

    def get_birthdayAlertMessage_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.birthday_alert_message))

    def get_identificationAlertMessage_element(self): # abonelikler için zorunlu alan
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.identificationNumber_alert_message))
    
    def get_invalid_identificationAlertMessage_element(self): # 11 haneden az/çok
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(mg_locate.invalid_identification_alert_message))

    def get_countryAlertMessage_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.country_alert_message))

    def get_cityAlertMessage_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.city_alert_message))

    def get_districtAlertMessage_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.district_alert_message))
    
    def get_addressAlertMessage_element(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(mg_locate.address_alert_message))
    
    def get_aboutAlertMessage_element(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(mg_locate.about_alert_message))
    