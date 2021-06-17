from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

def scrapingfunction(request): #requestオブジェクトを受け取る
    returnedObject = 'Hello world'
    return  HttpResponse(returnedObject) # responceオブジェクトを返す

def testfunc(request):
    #site = requests.get('https://www.google.com')
    site = requests.get('https://connpass.com/dashboard/')
    site = requests.get('https://www.fe-siken.com/')
    
    
    #print(site.text)    # site.text ->HTML
    data = BeautifulSoup(site.text, 'html.parser')
    
    tag1 = data.select_one('div', class_='mondai')
    #print(tag1)
    tag1_text=tag1.get_text()
    print(tag1_text) 

    return HttpResponse('test is done.')

