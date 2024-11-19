import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from colorama import Fore, Style, init

if len(sys.argv) != 2:
    print("Usage: python getpuzzle.py <cipher>")
    sys.exit(1)

Cipher = sys.argv[1]

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
driver.get('https://quipqiup.com/')

ciphertext_input = driver.find_element(By.XPATH, '//*[@id="ciphertext"]')
ciphertext_input.send_keys(Cipher)
time.sleep(2)

solve_button = driver.find_element(By.XPATH, '//*[@id="solve_button"]')
solve_button.click()
time.sleep(5)

decoded_message = driver.find_element(By.XPATH, '/html/body/div[4]/center[1]/table/tbody/tr[1]/td[3]')

print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} {decoded_message.text}")

time.sleep(5)
driver.quit()
