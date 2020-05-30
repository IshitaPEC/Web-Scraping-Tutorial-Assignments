import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

#In order to add the header to the request there we go
ua = UserAgent()
header={'user-agent':ua.chrome}

response= requests.get("https://codingbat.com/java",headers=header)
soup= BeautifulSoup(response.content,'html.parser')

tags= soup.find_all('div',attrs={'class':'summ'})
list_main=[]

for tag in tags:
    list_main.append('https://codingbat.com/'+ tag.a['href'])

for ch in list_main:
    response = requests.get(ch, headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    ele= soup.find_all('td',attrs={'width':200})
    for element in ele:
        url= 'https://codingbat.com'+ element.a['href']
        ref= element.a.string
        resp = requests.get(url, headers=header)
        sp =BeautifulSoup(resp.content,'html.parser')
        regex= re.compile(ref)
        examples= sp.find_all(string=regex)
        questions= sp.find_all('div',attrs={'class':'minh'})

#But the problem here is, that with regex and the method that you have used, what if there are only 2 examples, you cant simply assume 3 examples;
#Hence according to the structure you may choose the method of next_sibling, as many as next_siblings as we have!they would be printted
#Use questions[i].next_siblings
        for i in range(0,len(questions)):
            print("Question:")
            print(questions[i].p.string)
            #print(questions[i].next_sibling)
            list_ans= questions[i].next_siblings
            print("METHOD 1 EXAMPLES:")
           # print("Next Siblings:")
            for sibling in list_ans:
                if(sibling.string is not None):
                    print(sibling)
            #print("\n")
            print("METHOD 2 EXAMPLES:")
            print(examples[2])
            print(examples[3])
            print(examples[4])
            print("\n")
            print("\n")






