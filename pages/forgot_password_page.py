# Şifremi Unuttum Sayfası
# https://tobeto.com/sifremi-unuttum


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.loginPages.forgot_password_page import forgotPasswordPageLocators as fg_locate

class ForgotPaswordPage: 

    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def get_forgotPasswordTextbox_element(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(fg_locate.forgot_password_textbox))