from selenium import webdriver
from selenium.webdriver.common.keys import Keys
username = " "
password = " "


url = 'https://www.facebook.com/'
driver = webdriver.Chrome("Chrome_driver")
driver.get(url)

                          
element = driver.find_element_by_id("email")
element.send_keys(username)
elements = driver.find_element_by_id("pass")
elements.send_keys(password)
driver.find_element_by_id('loginbutton').click()                          




