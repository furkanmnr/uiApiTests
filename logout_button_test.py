from selenium import webdriver
from selenium.webdriver.common.by import By
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

# Logout bağlantısına tıkla
driver.find_element(By.LINK_TEXT, "Log Out").click()

time.sleep(2)

# Ana sayfaya dönüldü mü kontrol et
if "Customer Login" in driver.page_source:
    print("Çıkış işlemi başarıyla gerçekleşti.")
else:
    print("Çıkış işlemi başarısız.")

driver.quit()
