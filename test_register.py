from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/register.htm")

time.sleep(1)

# Form alanlarını doldur
driver.find_element(By.ID, "customer.firstName").send_keys("Bengü")
driver.find_element(By.ID, "customer.lastName").send_keys("Yanpar")
driver.find_element(By.ID, "customer.address.street").send_keys("Deneme Mah. 12. Sk.")
driver.find_element(By.ID, "customer.address.city").send_keys("Ankara")
driver.find_element(By.ID, "customer.address.state").send_keys("Çankaya")
driver.find_element(By.ID, "customer.address.zipCode").send_keys("06420")
driver.find_element(By.ID, "customer.phoneNumber").send_keys("05321234567")
driver.find_element(By.ID, "customer.ssn").send_keys("123-45-6789")

# Rastgele kullanıcı adı oluşturuyoruz
username = "bengu" + str(random.randint(1000, 9999))
driver.find_element(By.ID, "customer.username").send_keys(username)
driver.find_element(By.ID, "customer.password").send_keys("test123")
driver.find_element(By.ID, "repeatedPassword").send_keys("test123")

# Kayıt butonuna tıkla
driver.find_element(By.XPATH, "//input[@value='Register']").click()

time.sleep(2)

# Başarı mesajını kontrol et
if "Your account was created successfully" in driver.page_source:
    print(f"Kayıt başarılı. Kullanıcı adı: {username}")
else:
    print("Kayıt başarısız. Mesaj bulunamadı.")

driver.quit()
