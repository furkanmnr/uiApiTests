from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Tarayıcıyı başlat
driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/index.htm")

# Kullanıcı adı ve şifreyi boş bırak, doğrudan login tıkla
driver.find_element(By.NAME, "username").send_keys("")
driver.find_element(By.NAME, "password").send_keys("")
driver.find_element(By.XPATH, "//input[@value='Log In']").click()

time.sleep(2)

# Hata mesajı var mı kontrol et (beklenen mesaj)
if "Please enter a username and password." in driver.page_source:
    print("Boş giriş test PASSED. Hata mesajı gösterildi.")
elif "The username and password could not be verified." in driver.page_source:
    print("Boş giriş test PASSED. Sistemde doğrulama reddedildi.")
else:
    print("Boş giriş testi FAILED. Beklenen mesaj yok.")

driver.quit()
