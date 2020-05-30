from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

ua=UserAgent()
header= {'user-agent':ua.chrome}
response= requests.get("http://example.com/",headers=header)

soup =BeautifulSoup(response.content, 'html.parser')

#Accessing children via .contents->Yields me direct children only and returns a list:
contents= soup.head.contents
print(contents)

print("\n")
print("\n")
print("\n")

#Accessing children via .children -> Returns an iterator to save the space of a list-> yields only direct children
children= soup.head.children
for child in children:
    print(child if child is not None else '')


print("\n")
print("\n")
print("\n")

#Accessing children via descendants-> This also yields indirect children-> all children of children are also presented
for index,variables in enumerate(soup.head.descendants):
    print(index)
    print(variables)
    

