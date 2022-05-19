from selenium.webdriver.common.by import By

class PayPageLocators:
  CARD_NUMBER = (By.XPATH, "//input[@class='card-number']")
  CARD_USER = (By.XPATH, "")
  CVC = (By.XPATH, "//div[@class='cvv-input']/input")
  INPUT_CARD_DATA_TXT = (By.XPATH, "//h4")
  CARD_DATE_MONTH = (By.XPATH, "//div[@class='month']/input")
  CARD_DATE_YEAR = (By.XPATH, "//div[@class='year']/input")
  PAY_BUTTON = (By.XPATH, "//button")
