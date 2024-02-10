
# Profil Bilgileri -> Eğitim Hayatım Düzenleme sayfası Locators
# https://tobeto.com/profilim/profilimi-duzenle/egitim-hayatim

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.profileInfoPages.myeducationlife_page import MyeducationlifePageLocators as my_locate

class myeducationlife_page: 
    
    def get_save_button_element(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.save_button))

    def get_error_message1(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.error_message1))
    
    def get_error_message2(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.error_message2))
    
    def get_error_message3(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.error_message3))
    
    def get_error_message4(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.error_message4))
    
    def get_error_message5(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.error_message5))
    
    def get_error_message6(self):
        return  WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.error_message6))
    
    #test_myeducation_save_button
    def get_education(self):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(my_locate.education))

    def get_education_status(self):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(my_locate.education_status))
    
    def get_university(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.university))
    
    def get_department(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.departmen))
    
    def get_start_year(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.start_year))
    
    def get_start_year_calender(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.start_year_calender))
    
    def get_finish_year(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.finish_year))
    
    def get_finish_year_calender(self):
        return WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(my_locate.finish_year_calender))
    
    def get_toast_messageelement(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.toast_message))
    
    def get_delete_education_element(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.delete_education))
    
    def get_alert_message(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.alert_message))
    
    def get_yes_button(self):
        return  WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(my_locate.yes_button))