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

    # FORM ELEMENTS
    def get_corporationName_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.CORPORATION_NAME))
    
    def get_position_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.POSITION))

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
    
    # JOB DESC, DELETE EXPERINCE ELEMENTS
    def get_threeDotsButton_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(mg_locate.THREE_DOTS_BUTTON))
    
    def get_jobDesc_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.JOB_DESC))
    
    def get_closeButton_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.CLOSE_BUTTON))
    
    def get_deleteButton_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.DELETE_BUTTON))
    
    def get_deleteConfirmMessage_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.DELETE_CONFIRM_MESSAGE))
    
    def get_noButton_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.NO_BUTTON))
    
    def get_yesButton_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.YES_BUTTON))
    
    # necessary warning fields
    def get_corporationNameWarningField_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.CORPORATION_NAME_WARNING_FIELD))
    
    def get_positionWarningField_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.POSITION_WARNING_FIELD))
    
    def get_sectorWarningField_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.SECTOR_WARNING_FIELD))
    
    def get_startDateWarningField_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.START_DATE_WARNING_FIELD))
    
    def get_finishDateWarningField_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(mg_locate.FINISH_DATE_WARNING_FIELD))