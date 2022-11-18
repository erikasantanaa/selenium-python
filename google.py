from selenium.webdriver.common.by import By
from selenium import webdriver

from time import sleep

driver = webdriver.Chrome()

driver.get('https://google.com.br')

print(driver.current_url)
print(driver.title)
print(driver.capabilities["browserVersion"])


element = driver.find_element("name", "q")
element.click()
element.send_keys("Marvel")
element.submit()
sleep(3)

assert driver.title == "Marvel - Pesquisa Google"



driver.close()