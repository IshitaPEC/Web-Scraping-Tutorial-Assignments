#First we import webdriver from selenium
from selenium import webdriver
from time import sleep

#Create a driver object
#Make a web driver object
driver= webdriver.Chrome(r"C:\Users\Dell\Downloads\chromedriver_win32\chromedriver.exe")

#Get the url:
driver.get('https://www.instagram.com/')
#Search by xpath:
sleep(5)
tag= driver.find_element_by_xpath("//div[@id='react-root']//div[@class='gr27e']//a")
sleep(5)
tag.click()
sleep(5)
#Close the driver object
driver.close()

