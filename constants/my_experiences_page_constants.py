# Profil Bilgileri -> Deneyimlerim Sayfası Constants
# https://tobeto.com/profilim/profilimi-duzenle/deneyimlerim

# go to deneyimlerim page
USER_PROFILE_BUTTON_XPATH = "//*[@id='__next']/div/nav/div[1]/div/div/div[2]"

# form elements, add experience
CORPORATION_NAME_XPATH =  "//div[@id='__next']/div/main/section/div/div/div[2]/form/div/div/input"
POSITION_XPATH = "//div[@id=\'__next\']/div/main/section/div/div/div[2]/form/div/div[2]/input"
SECTOR_XPATH = "//div[@id=\'__next\']/div/main/section/div/div/div[2]/form/div/div[3]/input"
SELECT_COUNTRY_DROPDOWN_XPATH = "//div[@id=\'__next\']/div/main/section/div/div/div[2]/form/div/div[4]/select"
START_CALENDAR_XPATH =  "//div[@id=\'__next\']/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input"
START_DATE_CSS =  ".react-datepicker__day--020"
FINISH_CALENDAR_XPATH =  "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input"
FINISH_DATE_CSS = ".react-datepicker__day--026"
SAVE_BUTTON_XPATH =  ".btn-primary"

TOAST_MESSAGE_CSS =  ".toast-body"

# job description, delete experience
THREE_DOTS_BUTTON_XPATH = "//div[@id=\'__next\']/div/main/section/div/div/div[2]/div/div/div[2]/div[5]/span[2]"
JOB_DESC_XPATH = "//span[contains(.,\'İş Açıklaması\')]"
CLOSE_BUTTON_XPATH = "//button[contains(.,\'Kapat\')]"
DELETE_BUTTON_CSS = ".my-grade:nth-child(1) .grade-delete"
DELETE_CONFIRM_MESSAGE_XPATH = "//p[contains(.,\'Seçilen deneyimi silmek istediğinize emin misiniz ?\')]"
NO_BUTTON_XPATH = "//button[contains(.,\'Hayır\')]"
YES_BUTTON_XPATH = "//button[contains(.,\'Evet\')]"

# necessary warning fields
CORPORATION_NAME_WARNING_FIELD_CSS = ".col-12:nth-child(1) > .text-danger"
POSITION_WARNING_FIELD_CSS = ".col-12:nth-child(2) > .text-danger"
SECTOR_WARNING_FIELD_CSS = ".col-12:nth-child(3) > .text-danger"
START_DATE_WARNING_FIELD_CSS = ".col-12:nth-child(5) > .text-danger"
FINISH_DATE_WARNING_FIELD_CSS = ".text-danger:nth-child(4)"

      