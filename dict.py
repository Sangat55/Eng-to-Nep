from bs4 import BeautifulSoup
import urllib
import urllib.request
import pyautogui
def choice11():
    choice1 = input("Enter q to exit and n to search new item: ")
    if(choice1 == 'q'):
        return False
    elif (choice1 == 'n'):
        return True
    

def search(query):
    address = "https://www.englishnepalidictionary.com/?q=%s" %(urllib.parse.quote_plus(query))
    getRequest = urllib.request.Request(address, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})
    urlfile = urllib.request.urlopen(getRequest)
    htmlResult = urlfile.read(200000)
    urlfile.close()
    soup  = BeautifulSoup(htmlResult,'lxml')
    
    h3 = soup.find('h3')
    for h in h3:
        return h
choice = True
while(choice):
    filename = input("Enter the english Word: ")
    meaning = search(filename)
    invalid = "Word not found!"
    if meaning != invalid:
        result= (meaning)
        print(result)
    else:
        print('Invalid:')
    choice = choice11()
