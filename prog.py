import requests

def getTitle(url):
   r = requests.get(url)
   cont = r.content

   start = cont.find('<title>')+7   # Find the position where the title starts
   end = cont.find('</title>',start)   # Find the position where the title ends
   if (start < 7):   # If a starting position was not found
                  # because the source code is written in capitals
      start = cont.find('<TITLE>')+7
      end = cont.find('</TITLE>',start)
   
   return cont[start:end]
url = raw_input("Provide a full URL of a website:")
print getTitle(url)