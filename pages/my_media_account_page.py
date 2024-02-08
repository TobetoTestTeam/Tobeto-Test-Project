from selenium import webdriver

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.profileInfoPages.my_media_accounts_page import add_media_acconts_Locators as ma_locate

class MediaAccountPage: 
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def get_dropdown_button_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((ma_locate.dropdown)))
    
    def get_media_url_text_element(self):
        return WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((ma_locate.media_url)))
    
    def get_save_button_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((ma_locate.save_button)))
    
    def get_toastbody_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((ma_locate.toast_body)))
    
    def get_warning_message1_element(self):
        return  WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((ma_locate.warning_message1)))
    
    def get_warning_message2_element(self):
        return  WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((ma_locate.warning_message2)))
    
    def get_unsuccessful_toastbody_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((ma_locate.unsuccessful_toast_body)))
    
    def get_delete_button_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((ma_locate.delete_button)))
    
    def get_delete_yes_button_element(self):
         return  WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((ma_locate.delete_yes_button)))
    
    def get_delete_no_button_element(self):
         return  WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((ma_locate.delete_no_button)))
    
    def get_delete_toastbody_element(self):
        return WebDriverWait(self.driver, 0,5).until(ec.presence_of_element_located((ma_locate.delete_toast_body)))
    
    def get_3media_account_element(self):
        return  WebDriverWait(self.driver, 0.5).until(ec.visibility_of_element_located((ma_locate.media_3_message)))
    
    def get_pencil_button_element(self):
        return WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((ma_locate.pencil_button)))
    
    def get_edit_text_element(self):
        return WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((ma_locate.edit_text)))
    
    def get_update_button_element(self):
        return WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((ma_locate.update_button)))
    
    def get_update_toastbody_element(self):
        return WebDriverWait(self.driver, 0,5).until(ec.presence_of_element_located((ma_locate.update_toast_body)))
    