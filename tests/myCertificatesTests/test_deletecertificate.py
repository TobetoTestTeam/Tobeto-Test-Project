
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep
import pytest
from pages.certificate_page import CertificatePage
import tests.loginTests.test_validLogin as login

class TestDeletecertificate():
  def setup_method(self):
    valid_login = login.TestvalidLogin()
    valid_login.setup_method()
    valid_login.test_validLogin()
    self.driver = valid_login.getDriver()
  
  def teardown_method(self):
    self.driver.quit()
  
  @pytest.mark.skip()
  def test_deletecertificate(self):
    self.driver.get("https://tobeto.com/profilim/profilimi-duzenle/sertifikalarim")
    
    dustbin_button=CertificatePage.get_dustbin_button_element(self)
    dustbin_button.click()
    yes_button=CertificatePage.get_yes_button_element(self)
    yes_button.click()
    information_popup=CertificatePage.get_delete_certificateTextbox_element(self)
    assert information_popup.text == "• Dosya kaldırma işlemi başarılı."
