import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua=UserAgent()
header= {'user-agent':ua.chrome}
response= requests.get("http://example.com/",headers=header)

soup= BeautifulSoup(response.text, 'html.parser')

#Access Contents to see what all tags are present and the tree structure
print(soup.html.contents)

#Access next sibling
print(soup.h1.next_sibling.next_sibling.name)

#Previous Sibling
print(soup.p.previous_sibling.previous_sibling.name)

#Next Siblings list
for sibling in soup.h1.next_siblings:
    print(sibling.name)

#Previous Siblings list
#Essential
for sibling in soup.p.previous_siblings:
    print(sibling.name)
