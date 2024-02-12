# Login Page 
# https://tobeto.com/giris

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.loginPages.login_page import LoginPageLocators as lg_locate

class LoginPage: 

    def gotoPage(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()

    def get_username_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(lg_locate.user_email))
    
    def get_password_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(lg_locate.user_password))
    
    def get_girisButton_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(lg_locate.giris_button))
    
    def get_warningFieldMail_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(lg_locate.warning_field_mail))
    
    def get_warningFieldPass_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(lg_locate.warning_field_pass))
    
    def get_toastMessage_element(self):
        return WebDriverWait(self.driver, 500).until(ec.presence_of_element_located(lg_locate.toast_message))
