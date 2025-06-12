from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Giriş bilgileri
username = "furkanmnr"
password = "12345"

# Tarayıcıyı başlat
driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/index.htm")

# Giriş işlemi
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.XPATH, "//input[@value='Log In']").click()

time.sleep(2)

# "Open New Account" sayfasına git
driver.find_element(By.LINK_TEXT, "Open New Account").click()

time.sleep(1)

#SAVINGS veya CHECKING
account_type_dropdown = Select(driver.find_element(By.ID, "type"))
account_type_dropdown.select_by_visible_text("SAVINGS")

existing_account_dropdown = Select(driver.find_element(By.ID, "fromAccountId"))
existing_account_dropdown.select_by_index(0)

# Submit (Aç butonuna tıkla)
driver.find_element(By.XPATH, "//input[@value='Open New Account']").click()

time.sleep(2)

# Başarı mesajı kontrolü
if "Account Opened!" in driver.page_source:
    print("Yeni hesap başarıyla açıldı.")
else:
    print("Hesap açma başarısız veya mesaj görüntülenemedi.")

driver.quit()
