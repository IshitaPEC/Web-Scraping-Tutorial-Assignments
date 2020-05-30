import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

#In order to add the header to the request there we go
ua = UserAgent()
header={'user-agent':ua.chrome}

response= requests.get("https://boston.craigslist.org/search/sof",headers=header)
soup= BeautifulSoup(response.content,'html.parser')
#print(soup.prettify())


attr={'class':'result-title hdrlnk'}
c= soup.find_all('a',attrs=attr)
for tag in c:
    print("Job:",tag.text)
    print("URL:",tag['href'])
