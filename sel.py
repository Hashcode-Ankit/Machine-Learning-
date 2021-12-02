from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

url="https://www.pepcoding.com/login"
id="pemail@gmail.com"
passwd="pass"
browser=webdriver.Chrome(executable_path="C:\\Users\\Ankit Sharma\\Downloads\\chromedriver.exe")

browser.get(url)
# time.sleep(1)

username = browser.find_element(By.NAME, 'email')
username.send_keys(id)

password = browser.find_element(By.NAME, 'password')
password.send_keys(passwd)

login = browser.find_element(By.XPATH, '//button')
login.click()   