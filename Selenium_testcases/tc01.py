from selenium.webdriver.support.select import Select
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

d=webdriver.Chrome()
d.maximize_window()
d.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

d.find_element(By.CSS_SELECTOR,'input[name="username"]').send_keys('Y Chiranjeevi')

d.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys('Ravi@123')

a=d.find_element(By.TAG_NAME,"textarea")

a.clear()

a.send_keys("This is about my automation testing online in the free testing source")

sleep(2)

wait = WebDriverWait(d, 10)
b = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="filename"]')))


b.send_keys(r"C:\Users\ycycr\OneDrive\Pictures\ac.jpg")

d.execute_script("window.scrollTo(0,800)")


d.find_element(By.CSS_SELECTOR,'input[value="cb1"]').click()


d.find_element(By.CSS_SELECTOR,'input[value="rd3"]').click()

Select(d.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[7]/td/select')).select_by_index(1)
Select(d.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[7]/td/select')).select_by_index(3)

Select(d.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[8]/td/select')).select_by_index(5)


d.find_element(By.XPATH,'//input[@value="submit"]').click()  
sleep(10)