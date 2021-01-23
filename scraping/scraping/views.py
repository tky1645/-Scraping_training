from django.http import HttpResponse

def scrapingfunction(request): #requestオブジェクトを受け取る
    returnedObject = 'Hello world'
    return  HttpResponse(returnedObject) # responceオブジェクトを返す

