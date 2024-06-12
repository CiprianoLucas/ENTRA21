import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

class SupplierRegister:
    def __init__(self, driver_path, csv_path):
        self.driver_path = driver_path
        self.csv_path = csv_path
        self.max_workers = math.floor(os.cpu_count() / 2) or 2
        
    def setup_driver(self):
        service = webdriver.ChromeService(executable_path=self.driver_path)
        driver = webdriver.Chrome(service=service)
        
        return driver
    
    def login(self, driver):
        driver.get("http://localhost:8000/admin")
        driver.find_element(By.ID, "id_username").send_keys("admin")
        driver.find_element(By.ID, "id_password").send_keys("admin", Keys.RETURN)
        
    def add_supplier(self, row):
        driver = self.setup_driver()
        self.login(driver)
        
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

        driver.close()
        
    def run(self):
        df = pd.read_csv(self.csv_path, sep=";")
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            executor.map(self.add_supplier, df.to_dict('records'))          

if __name__ == "__main__":
    DRIVER_PATH = r"C:\Users\Lucas Cipriano\Documents\ENTRA21\Modulo 9 - Web Screpy\Aula 3\chromedriver.exe"
    CSV_PATH = r"C:\Users\Lucas Cipriano\Documents\ENTRA21\Modulo 9 - Web Screpy\Aula 3\suppliers.csv"
    
    register = SupplierRegister(DRIVER_PATH, CSV_PATH)
    register.run()