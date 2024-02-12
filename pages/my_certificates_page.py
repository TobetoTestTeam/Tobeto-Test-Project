from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.profileInfoPages.my_certificates_page import certificate_Locators as dc_locate

class CertificatePage: 
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_delete_certificateTextbox_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((dc_locate.information_popup)))
    
    def get_dustbin_button_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((dc_locate.dustbin_button)))
    
    def get_yes_button_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((dc_locate.yes_button)))
    
    def get_no_button_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((dc_locate.no_button)))
    
    def get_dowland_button_element(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((dc_locate.dowland_button)))