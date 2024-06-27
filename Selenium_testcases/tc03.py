from selenium.webdriver.support.select import Select
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

##Initialise browser ,goto link and maximize the browser
d = webdriver.Chrome()
d.get('https://testautomationpractice.blogspot.com/')
d.maximize_window()

##Input fields
name=d.find_element(By.ID,'name').send_keys('Y Chiranjeevi')
email=d.find_element(By.ID,'email').send_keys('Chiruteja135@gmail.com')
Phone=d.find_element(By.ID,'phone').send_keys('9493595563')
Address=d.find_element(By.ID,'textarea').send_keys("Venugopal Nagar,Anantapur")
sleep(5)
##  scroll dows
d.execute_script("window.scrollTo(0,600)")

## Radio buttons,Check boxex,Multiple values,Dropdown values,Date
gender=d.find_element(By.ID,'male').click()
days=d.find_element(By.ID,'thursday').click()
country=d.find_element(By.XPATH,"//option[@value='india']").click()
colors=Select(d.find_element(By.ID,'colors')).select_by_index(0)
colors=Select(d.find_element(By.ID,'colors')).select_by_index(2)
days=d.find_element(By.ID,'datepicker').send_keys('05/05/1994')
d.execute_script("window.scrollTo(600,1000)")
sleep(5)
##Table data
book_name=[book.text for book in d.find_elements(By.XPATH,"//div[@class='widget-content']//tbody//tr//td[1]")]
names_only = [name for name in book_name if not name.isdigit()]
print("Book Names",names_only)
sleep(5)

##Tableselect boxes and values
d.find_element(By.XPATH,'//*[@id="productTable"]/tbody/tr[2]/td[4]/input').click()
d.find_element(By.XPATH,'//*[@id="productTable"]/tbody/tr[4]/td[4]/input').click()
sleep(5)

# price_list=[price.text for price in d.find_elements(By.XPATH,"//table[@Id='productTable']/thead/tr[1]/th[3]")]
# print("Prices:",price_list)

price_list = [price.text for price in d.find_elements(By.XPATH, "//table[@id='productTable']/tbody/tr/td[3]")]
print("Prices:", price_list)

product_names=[product.text for product in d.find_elements(By.XPATH,"//table[@Id='productTable']/tbody/tr/td[2]")]
print("Product names",product_names)
sleep(5)

d.find_element(By.ID,'Wikipedia1_wikipedia-search-input').send_keys('India')
d.find_element(By.XPATH,'//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input').click()
d.find_element(By.XPATH,'//*[@id="HTML4"]/div[1]/button').click()
sleep(5)
d.switch_to(window_handles[0])
sleep(10)