from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Giriş bilgileri (daha önce register.py ile oluşturulan kullanıcı olmalı)
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

# Transfer Funds sayfasına git
driver.find_element(By.LINK_TEXT, "Transfer Funds").click()

time.sleep(1)


driver.find_element(By.ID, "amount").send_keys("500")
from_account = driver.find_element(By.ID, "fromAccountId")
to_account = driver.find_element(By.ID, "toAccountId")


from_account.click()
to_account.click()

# Transfer butonuna tıkla
driver.find_element(By.XPATH, "//input[@value='Transfer']").click()

time.sleep(2)

# Başarı mesajı kontrolü yapıyoruz
if "Transfer Complete!" in driver.page_source:
    print("Transfer başarılı şekilde gerçekleşti.")
else:
    print("Transfer başarısız veya mesaj bulunamadı.")

driver.quit()
