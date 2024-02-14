# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import tests.loginTests.test_validLogin as login
from time import sleep
from pages.my_media_account_page import MediaAccountPage

class TestDeletemediaaccount():
  def setup_method(self, method):
    valid_login = login.TestvalidLogin()
    valid_login.setup_method()
    valid_login.test_validLogin()
    self.driver = valid_login.getDriver()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_deletemediaaccount(self):
    self.driver.get("https://tobeto.com/profilim/profilimi-duzenle/medya-hesaplarim")
    #self.driver.set_window_size(1382, 744)
    delete_button=MediaAccountPage.get_delete_button_element(self)
    delete_button.click()
    yes_button=MediaAccountPage.get_delete_yes_button_element(self)
    yes_button.click()
    toast_body=MediaAccountPage.get_delete_toastbody_element(self)
    assert toast_body.text == "• Sosyal medya adresiniz başarıyla kaldırıldı."
  