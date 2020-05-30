from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
#PURPOSE OF USER_AGENTS: The purpose of user agents is to add a fake header in my request while requesting for a response from the browser. This is to prove your authenticity
#Any browsers request is acceptable however if a user constantly requests then it might be suspicious hence we add this explicit header

#In requirements.txt file write 'fake_user_agent'
ua= UserAgent()
header= {'user-agent':ua.chrome}
print(ua.chrome)

page= requests.get('https://www.google.com',headers=header,timeout=3)
print(page.content)

soup = BeautifulSoup(page.content,'html.parser')
print(soup.meta['charset'])
print(soup.meta.get('charset'))
print(soup.title)
print(soup.title.string)
#soup.tittle.string.replace_with("Yahoo")
#print(soup.title.string)

