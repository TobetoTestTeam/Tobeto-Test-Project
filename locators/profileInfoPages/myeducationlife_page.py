



from selenium.webdriver.common.by import By
import constants.myeducationlife_constants as me

class MyeducationlifePageLocators:
    save_button = (By.CSS_SELECTOR,me.SAVE_BUTTON_CSS )
    error_message1 = (By.CSS_SELECTOR,me.ERROR_MESSAGE1)
    error_message2 = (By.CSS_SELECTOR,me.ERROR_MESSAGE2)
    error_message3 = (By.CSS_SELECTOR,me.ERROR_MESSAGE3 )
    error_message4 = (By.CSS_SELECTOR,me.ERROR_MESSAGE4)
    error_message5 = (By.CSS_SELECTOR,me.ERROR_MESSAGE5)
    error_message6 = (By.CSS_SELECTOR,me.ERROR_MESSAGE6 )
    education = (By.NAME,me.EDUCATION )
    education_status = (By.NAME, me.EDUCATION_STATUS)
    university = (By.NAME, me.UNIVERSITY)
    departmen = (By.NAME, me.DEPARTMENT )
    start_year = (By.XPATH,me.START_YEAR)
    start_year_calender = (By.CSS_SELECTOR,me.START_YEAR_CALENDER)
    finish_year = (By.XPATH,me.FINISH_YEAR)
    finish_year_calender = (By.XPATH,me.FINISH_YEAR_CALENDER)
    toast_message = (By.CSS_SELECTOR,me.TOAST_MESSAGE)
    delete_education = (By.CSS_SELECTOR,me.DELETE_EDUCATION )
    alert_message = (By.CSS_SELECTOR,me.ALERT_MESSAGE )
    yes_button = (By.CSS_SELECTOR,me.YES_BUTTON )