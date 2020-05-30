import requests

#Response object-> Implies just as if we are opening a web_page
#2 types of requests: GET,POST
#GET: Retrieval of data
#POST: Sending data

response= requests.get('https://www.google.com')
print(response)

#Print response content->precisely, the source code:
print(response.content)

#Status Code->Success/Failure
#1XX->Informational
#2XX->Success
#3XX->Redirection
#4XX->Client Error
#5XX->Server Error
print(response.status_code)

#Headers->It exisits as a dictionary-> key value pair
print(response.headers)
