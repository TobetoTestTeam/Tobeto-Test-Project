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
    
    def get_birtday_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.birthday))
    
    def get_identificationNumber_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.identification_number))
    
    def get_country_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.country))
    
    def get_cityDropdown_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.city_dropdown))
    
    def get_districtDropdown_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.district_dropdown))
    
    def get_saveButton_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.save_button))