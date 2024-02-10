
from selenium.webdriver.common.by import By
import constants.competence as cd

class Competence:
   
   competence = (By.CSS_SELECTOR, cd.COMPETENCE)
   toast_message = (By.CSS_SELECTOR, cd.TOAST_MESSAGE )
   competence_delete = (By.CSS_SELECTOR,cd.COMPETENCE_DELETE )
   delete_button = (By.CSS_SELECTOR,cd.DELETE_BUTTON )