from bs4 import BeautifulSoup
import requests

bczs = "http://ip.bczs.net/"


def getText(url):
    contents = requests.get(url + 'countrylist')
    text = contents.text
    return text

def getCountryList(text):
    # soup = BeautifulSoup(text, 'html.parser')
    # tds = BeautifulSoup(text, 'html.parser').find_all('td',{'class': 'r'})
    countryList = []
    for td in BeautifulSoup(text, 'html.parser').find_all('td',{'class': 'r'}):   
        for aTag in td.contents:
            countryList.append(aTag['href'])
    return countryList

text = getText(bczs)
countrys = getCountryList(text)
print(countrys)

