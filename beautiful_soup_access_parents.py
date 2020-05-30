import requests
from bs4 import BeautifulSoup

from fake_useragent import UserAgent

ua=UserAgent()
header= {'user-agent':ua.chrome}
print(ua.chrome)

response= requests.get("http://example.com/",headers=header)

soup= BeautifulSoup(response.text, 'html.parser')
#Access parents of a given tag
body=soup.body
html= soup.html
print(body.parent.name)
print(html.parent.name)

#Access all parents together
for parent in body.parents:
    print(parent.name)

