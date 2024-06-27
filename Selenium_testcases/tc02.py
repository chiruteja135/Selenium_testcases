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
d.get("https://rahulshettyacademy.com/AutomationPractice/")

d.implicitly_wait(30)
## ⦁	SELECT RADIO BUTTON 2
d.find_element(By.CSS_SELECTOR,'input[value="radio2"]').click()

## ⦁	ENTER TEXT INTO TEXT BOX
d.find_element(By.ID,'autocomplete').send_keys('Bharath')

## ⦁	SELECT DROPDOWN VALUE OPTION-2
Select(d.find_element(By.ID,"dropdown-class-example")).select_by_index(1)

## ⦁	SELECT CHECKBOX 2
d.find_element(By.ID,"checkBoxOption2").click()

## ⦁	CLICK ON OPEN WINDOW BUTTON AND GET TITLE OF NEW WINDOW AND VALIDATE
bt=d.find_element(By.ID,"openwindow")
bt.click()
bt_title=d.title
assert bt_title =='Practice Page','TiltleNotMatchException'

## ⦁	CLICK ON OPEN TAB BUTTON AND GET TITLE OF NEW TAB AND VALIDATE
bd=d.find_element(By.LINK_TEXT,"Open Tab")
bd.click()
bd_title=d.title
assert bd_title =='Practice Page','TiltleNotMatchException'


# Assuming 'd' is your WebDriver instance
window_handles = d.window_handles
d.switch_to.window(window_handles[0])

# ⦁	ENTER YOUR NAME IN TEXT BOX THEN CLICK ON ALERT THEN CLICK ON OK BUTTON IN ALERT
d.find_element(By.ID,'name').send_keys('Y Chiranjeevi')
d.find_element(By.ID,'alertbtn').click()
alert=d.switch_to.alert
alert.accept()

##⦁	ENTER YOUR NAME IN TEXT BOX THEN CLICK ON CONFIRM THEN CLICK ON CANCEL BUTTON IN ALERT
d.find_element(By.ID,'name').send_keys('Y Chiranjeevi')
d.find_element(By.ID,'confirmbtn').click()
alert=d.switch_to.alert
alert.dismiss()

d.execute_script("window.scrollTo(0,500)")

##.   READ ALL PRICE DETAILS FROM TABLE 
prices = [price.text for price in d.find_elements(By.XPATH, '//*[@id="product"]/tbody/tr/td[3]')]
# print("Price",prices)
integers = [int(i) for i in prices if i.isdigit()]
print(integers)

## READ ALL THE NAMES 
names = [name.text for name in d.find_elements(By.XPATH,"//*[@class='tableFixHead']//tbody/tr/td[1]")]
print("Names:", names)
# sleep(10)