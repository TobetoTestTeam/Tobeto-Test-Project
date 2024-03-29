# Test Senaryosunun Adı: Kayıt Ol
# TEST CASE 3: Geçersiz Eposta ve doldurması zorunlu alan kontrolü 
# (TEST case bu şekilde yazılmış ama burada sadece geçersiz e posta girildiğinde alınacak uyarı test ediliyor.)

# Kayıt Ol sayfası 
# https://tobeto.com/kayit-ol

# Generated by Selenium IDE
import pytest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep

from pages.register_page import RegisterPage, RegisterPageWindow

class TestInvalidEmail():
  def setup_method(self):
    #self.driver = webdriver.Chrome()
    #self.driver.get("https://tobeto.com/kayit-ol")
    #self.driver.maximize_window()
    RegisterPage.gotoPage(self)
    self.driver.delete_all_cookies()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()


  #@pytest.mark.skip() 
  def test_invalidEmail(self):
  
    
    email = RegisterPage.get_email_element(self)
    email.send_keys("notAnEmail.")
    
    
    invalidEmailAlert = RegisterPage.get_invalidEmailAlert_element(self)
    invalidEmailAlert_text = invalidEmailAlert.text
    assert invalidEmailAlert_text == "Geçersiz e-posta adresi*"
    sleep(5)
  
