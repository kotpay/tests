from selenium.webdriver.common.by import By

class PayPageLocators:
  CARD_NUMBER = (By.XPATH, "//input[@class='card-number']")
  CARD_USER = (By.XPATH, "//input[@placeholder='Card Holder']")
  CVC = (By.XPATH, "//div[@class='cvv-input']/input")
  INPUT_CARD_DATA_TXT = (By.XPATH, "//h4")
  CARD_DATE_MONTH = (By.XPATH, "//div[@class='month']/input")
  CARD_DATE_YEAR = (By.XPATH, "//div[@class='year']/input")
  PAY_BUTTON = (By.XPATH, "//button")
  SUCCESS_MESSAGE_TXT = (By.XPATH, "//b[text()='Транзакция прошла успешно.']")
  UNSUCCESS_MESSAGE_TXT = (By.XPATH, "//b[text()='К сожалению погашение не удалось.']")
  PAGE_BUTTON = (By.XPATH, "//button")
  MONTH = (By.XPATH, "//input[@placeholder='month']")
  YEAR = (By.XPATH, "//input[@placeholder='year']")
