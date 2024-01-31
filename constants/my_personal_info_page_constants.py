# Profil Bilgileri -> Kişisel Bilgilerim Sayfası CONSTANTS
# https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim

import os

FIRST_NAME_BYNAME = "name"
LAST_NAME_BYNAME = "surname"
PHONE_NUMBER_BYID = "phoneNumber"
BIRTHDAY_BYNAME = "birthday"
IDENTIFICATION_NUMBER_BYNAME = "identifier"

IDENTIFICATION_NUMBER = os.getenv("IDENTITY_NUM")

COUNTRY_BYNAME = "country"

CITY_DROPDOWN_BYNAME = "city"

DISTRICT_DROPDOWN_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/select"
DISTRICT_OPTION_XPATH = "//option[. = 'Adıyaman Merkez']"

SAVE_BUTTON_CSS = ".btn-primary"
SAVE_BUTTON_XPATH = "//button[contains(.,'Kaydet')]" # "/*[@id='__next']/div/main/section/div/div/div[2]/form/button"