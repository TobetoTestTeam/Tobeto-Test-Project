# Profil Bilgileri -> Yetkinliklerim Düzenleme sayfası Locators
# https://tobeto.com/profilim/profilimi-duzenle/yetkinliklerim

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.profileInfoPages.competence import Competence


class competence_add:
 def get_competence_add(self):
    return  WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(Competence.competence))
 
 def get_toast_message(self):
   return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(Competence.toast_message))
 
class Competence_delete:
  def get_competence_delete(self):
    return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(Competence.competence_delete))
  
  def get_delete_button(self):
    return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(Competence.delete_button))
  
  def get_toast_message(self):
   return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(Competence.toast_message))
 