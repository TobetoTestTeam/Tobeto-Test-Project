from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.platformPages.my_profile_page import myprofile_Locators as mp_locate

class MyProfilePage: 
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_edit_button_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((mp_locate.edit_button)))
    
    def get_myprofile_element(self):
        return WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((mp_locate.my_personal_info)))
    
    def get_eye_button_element(self):
        return WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((mp_locate.eye_button)))
    
    def get_result_page_element(self):
        return WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((mp_locate.result_page)))