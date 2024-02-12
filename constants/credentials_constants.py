# login page credential constants
# https://tobeto.com/giris

import os

USER_MAIL = os.getenv("user_mail_env") 
USER_PASSWORD = os.getenv("user_password_env")

# my personal info page credential constants
# https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim
IDENTIFICATION_NUMBER = os.getenv("IDENTITY_NUM")
IDENTITY_NAME = os.getenv("IDENTITY_name")
IDENTITY_SURNAME = os.getenv("IDENTITY_surname")
IDENTITY_BIRTHDATE = os.getenv("IDENTITY_birthdate")