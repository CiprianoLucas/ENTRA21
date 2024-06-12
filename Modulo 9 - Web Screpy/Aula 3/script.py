from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

DRIVER_PATH = r"C:\Users\Lucas Cipriano\Documents\ENTRA21\Modulo 9 - Web Screpy\Aula 3\chromedriver.exe"

service = webdriver.ChromeService(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:8000/admin")

username_input = driver.find_element(By.ID, "id_username")
username_input.send_keys("admin")

password_input = driver.find_element(By.ID, "id_password")
password_input.send_keys("admin")

password_input.send_keys(Keys.RETURN)


CSV_PATH = r"C:\Users\Lucas Cipriano\Documents\ENTRA21\Modulo 9 - Web Screpy\Aula 3\suppliers.csv"
df = pd.read_csv(CSV_PATH, sep=";")

for index, row in df.iterrows():
    driver.get("http://localhost:8000/empresas/cadastro") 
     
    driver.find_element(By.ID, "id_username").send_keys(row["company_name"].replace(" ", ""))
    driver.find_element(By.ID, "id_fantasy_name").send_keys(row["fantasy_name"])
    driver.find_element(By.ID, "id_cnpj").send_keys(row["cnpj"])
    driver.find_element(By.ID, "id_phone").send_keys(row["phone"])
    driver.find_element(By.ID, "id_email").send_keys(row["email"])
    driver.find_element(By.ID, "id_representative").send_keys(row["representative"])
    driver.find_element(By.ID, "id_street").send_keys(row["street"])
    driver.find_element(By.ID, "id_zipcode").send_keys(row["zipcode"])
    driver.find_element(By.ID, "id_number").send_keys(row["number"])
    driver.find_element(By.ID, "id_city").send_keys(row["city"])
    driver.find_element(By.ID, "id_state").send_keys(row["state"])
    driver.find_element(By.ID, "id_password").send_keys("123")
    driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/form/button').send_keys(Keys.RETURN)
    

while True:
    ...

# driver.close()