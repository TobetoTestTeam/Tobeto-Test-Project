# Şifremi Unuttum
# Test Senaryosunun Adı: Şifre sıfırlama kontrolleri
# TEST CASE 1: Başarılı Şifre sıfırlama işlem kontrolü

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from pages.forgot_password_page import ForgotPaswordPage

class TestSuccessPasswordReset():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get("https://tobeto.com/sifremi-unuttum")
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_successPasswordReset(self):
    
    sifremi_unuttum_textbox = ForgotPaswordPage.get_forgotPasswordTextbox_element(self)
    sifremi_unuttum_textbox.send_keys("test@gmail.com")

    gonder_button = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".btn:nth-child(3)")))
    gonder_button.click()
    
    uyari_mesaj = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
    assert uyari_mesaj.text == "• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."
    self.driver.close()
  
