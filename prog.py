import requests

def getTitle(url):
   r = requests.get(url)
   cont = r.content

   start = cont.find('<title>')+7   # Find the position where the title starts
   end = cont.find('</title>',start)   # Find the position where the title ends

   return cont[start:end]