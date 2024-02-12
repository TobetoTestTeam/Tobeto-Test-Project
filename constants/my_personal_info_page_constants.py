# Profil Bilgileri -> Kişisel Bilgilerim Sayfası CONSTANTS
# https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim

FIRST_NAME_BYNAME = "name"
LAST_NAME_BYNAME = "surname"
PHONE_NUMBER_BYID = "phoneNumber"
BIRTHDAY_BYNAME = "birthday"
IDENTIFICATION_NUMBER_BYNAME = "identifier"

COUNTRY_BYNAME = "country"

CITY_DROPDOWN_BYNAME = "city"

DISTRICT_DROPDOWN_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/select"
DISTRICT_OPTION_XPATH = "//option[. = 'Adıyaman Merkez']"

ADDRESS_BYNAME = "address"
ABOUT_CSS = ".col-12:nth-child(12) > .form-control" 

SAVE_BUTTON_CSS = ".btn-primary"
SAVE_BUTTON_XPATH = "//button[contains(.,'Kaydet')]" # "/*[@id='__next']/div/main/section/div/div/div[2]/form/button"

PAGE_TOAST_MESSAGE_CSS = ".toast-body"

# Invalid Input Alerts
USERNAME_ALERT_MESSAGE_CSS = ".col-12:nth-child(2) > .text-danger"
LASTNAME_ALERT_MESSAGE_CSS = ".col-12:nth-child(3) > .text-danger"
PHONENUMBER_ALERT_MESSAGE_CSS = ".col-12:nth-child(4) > .text-danger"
BIRTHDAY_ALERT_MESSAGE_CSS = ".col-12:nth-child(5) > .text-danger"
IDENTIFICATIONNUMBER_ALERT_MESSAGE_CSS = "i" # Abonelikler için zorunlu alan
INVALID_IDENTIFICATON_ALERT_MESSAGE_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span[2]" # 11 HANEDEN AZ/ÇOK
COUNTRY_ALERT_MESSAGE_CSS = ".col-12:nth-child(8) > .text-danger"
CITY_ALERT_MESSAGE_CSS = ".col-12:nth-child(9) > .text-danger"
DISTRICT_ALERT_MESSAGE_CSS = ".col-12:nth-child(10) > .text-danger"
ADDRESS_ALERT_MESSAGE_CSS = ".col-12:nth-child(11) > .text-danger"
ABOUT_ALERT_MESSAGE_CSS = ".col-12:nth-child(12) > .text-danger"