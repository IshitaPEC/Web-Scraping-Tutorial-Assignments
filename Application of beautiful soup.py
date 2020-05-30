import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re


def hastag(tag):
    return tag.has_attrs('href')

#In order to add the header to the request there we go
ua = UserAgent()
header={'user-agent':ua.chrome}

response= requests.get("http://example.com/",headers=header)
soup= BeautifulSoup(response.content,'html.parser')
print(soup.prettify())

#SIGNATUE-> find_all(name,attrs,recursive,string,limit,**kwargs)

##########################################################################
#NAME:
#->Normal string/tag
p=soup.find_all('p')
print(p)

#AS REGEX
#The tag must start with b
regex= re.compile('^b')
b= soup.find_all(regex)
print(b)

#AS REGEX
#The tag must contain h->html,head,h1
regex=re.compile('h')
h= soup.find_all(regex)
for tag in h:
    print(tag.name)

#AS  A MATTER OF LIST(It is not a regex):
tags= soup.find_all(['h1','title'])
print(tags)
#FUNCTIONS:
for tag in soup.find_all(hastag):
    print(tag)

##############################################################################
#ATTRIBUTES:
#Store attributes as a dictionary
attr= {'href':"https://www.iana.org/domains/example"}
first_a= soup.find_all('a',attrs=attr)
print(first_a)
#We may add multiple attributes to our attr dictionary to be able to add more than one filters:
#We can use the attributes in the absence of name as well

########################################################################
#LIMIT PARAMETER: Limits the number of results that we get
a_tags=soup.find_all('a',limit=2)
print(a_tags)

########################################################################
#STRINGS:
#We want to print the navigable strings which contain a particular string as substring:
regex= re.compile('omain')
print(soup.find_all(string=regex))

#####################################################################
#Kwargs: to beable to find attributes for which otherwise we use dictionary

#####################################################################
#Recursive->restrict entry  to a particular tag

#####################################################################
#FIND() -> Limit automatically adjusted to 1
tag=soup.find('p')
print(tag)

#####################################################################
