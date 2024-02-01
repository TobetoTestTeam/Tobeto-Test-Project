# Profil Bilgileri -> Kişisel Bilgilerim Sayfası 
# https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.profileInfoPages.my_experiences_page import myExperiencesPageLocators as mg_locate

class MyExperiencesPage: 

    def __init__(self):
        self.driver = webdriver.Chrome()
        
        #self.driver.get("https://tobeto.com/giris")
        #self.driver.maximize_window()
    
    def gotoPage(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()

    
    def get_corporationName_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.CORPORATION_NAME))
    
    def get_sector_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.SECTOR))
    
    def get_countryDropdown_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.SELECT_COUNTRY_DROPDOWN))
    
    def get_startCalendar_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.START_CALENDAR))
    
    def get_startDate_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.START_DATE))
    
    def get_finishCalendar_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.FINISH_CALENDAR))
    
    def get_finishDate_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.FINISH_DATE))
    
    def get_saveButton_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.SAVE_BUTTON))
    
    def get_toastMessage_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.TOAST_MESSAGE))