# Kayıt Ol sayfası 
# https://tobeto.com/kayit-ol

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.loginPages.register_page import RegisterPageLocators as rg_locate

class RegisterPage: 

    def __init__(self):
        self.driver = webdriver.Chrome()
        #self.driver.get("https://tobeto.com/giris")
        #self.driver.maximize_window()
    
    def gotoPage(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/kayit-ol")
        self.driver.maximize_window()

    def get_firstName_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(rg_locate.first_name))
    
    def get_lastName_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(rg_locate.last_name))
    
    def get_email_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(rg_locate.email))
    
    def get_invalidEmailAlert_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(rg_locate.invalid_email_alert))
    
    def get_password_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(rg_locate.password))
    
    def get_passwordAgain_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(rg_locate.password_again))
    
    def get_registerButton_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(rg_locate.register_button))

# Açılır pencere
# Kayıt oluşturmak için gerekli sözleşmeler
    
class RegisterPageWindow:
    
    def get_contactPermission_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(rg_locate.contact_permission))
    
    def get_membershipContrat_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(rg_locate.membership_contrat))
    
    def get_emailConfirmation_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(rg_locate.email_confirmation))
    
    def get_phoneConfirmation_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(rg_locate.phone_confirmation))
    
    def get_phoneNumberCountry_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(rg_locate.phone_number_country))
    
    def get_phoneNumber_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(rg_locate.phone_number))
    
    def get_continueButton_element(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(rg_locate.continue_button))