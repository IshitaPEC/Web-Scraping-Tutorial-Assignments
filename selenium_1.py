from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Make a web driver object
driver= webdriver.Chrome(r"C:\Users\Dell\Downloads\chromedriver_win32\chromedriver.exe")

#GET THE SITE THAT YOU ARE SEARCHING FOR:
driver.get('https://mail.google.com/mail/u/0/')

#CREATE SOUP OBJECT
#use the following procedure to get the source code
soup=BeautifulSoup(driver.page_source,'html.parser')
print(soup.prettify())

#METHOD 1 : FINDING ELEMENT VIA ID:
search_bar= driver.find_element_by_id("identifierId")
search_bar.send_keys('ishitaarora2708@gmail.com')

#Two ways of submitting my form: Manually click on the 'Enter button'-> find the button by its id and then click on it
#While inputting data, the input tag will obviously be present in the <form></form>, so automatically when you do search_bar.submit()-> the form submits

#next_button= driver.find_element_by_id('identifierNext')
#next_button.click()
search_bar.submit()
#Clsoe the web driver object:
driver.close()
