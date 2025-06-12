from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/index.htm")

# Giriş bilgilerini doldur
driver.find_element(By.NAME, "username").send_keys("furkanmnr")
driver.find_element(By.NAME, "password").send_keys("12345")
driver.find_element(By.XPATH, "//input[@value='Log In']").click()

# Sayfanın yüklenmesini bekle
time.sleep(3)

# Sayfa içeriğini yazdır
print(driver.page_source)

# Giriş başarılı mı kontrol et
if "Accounts Overview" in driver.page_source:
    print("Giriş başarılı, test geçti.")
else:
    print("Giriş başarısız, test kaldi.")

driver.quit()
