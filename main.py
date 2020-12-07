from plyer import notification;
import requests;
from bs4 import BeautifulSoup

def notifyMe(title,message):
    notification.notify(
        title = title,
        message =message,
        timeout = 6
    )
def getData(url):
    r = requests.get(url)
    return r.text    

if __name__ == "__main__":
    notifyMe("Kindi","Odra myre")    
    myhtmldata = getData("https://www.mohfw.gov.in/")
    print(myhtmldata)
    soup = BeautifulSoup(myhtmldata,'html.parser')
    print(soup.prettify)
    myDatastr = ""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myDatastr += tr.get_text() 
    itemList = myDatastr.split("\n\n")
    states = ['','']
    for item in itemList[0:22]:
        datalist = item.split("\n\n")
        if datalist[1]  in states:
            




