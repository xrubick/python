from bs4 import BeautifulSoup
import requests

bczs = "http://ip.bczs.net/"


def getText(url):
    contents = requests.get(url + "countrylist",headers={'Cache-Control': 'no-cache'})
    print(contents)
    text = contents.text
    print(text)
    return text

def getCountryList(text):
    # soup = BeautifulSoup(text, 'html.parser')
    # tds = BeautifulSoup(text, 'html.parser').find_all('td',{'class': 'r'})
    countryList = []
    for td in BeautifulSoup(text, 'html.parser').find_all('td',{'class': 'r'}):   
        for aTag in td.contents:
            countryList.append(aTag['href'])
    return countryList

def getCountryIPTable(uri):
    countryUrl = bczs + uri
    # contents = requests.get(countryUrl)
    text = requests.get(countryUrl).text
    table = BeautifulSoup(text,'html.parser').find_all('table')
    return table


text = getText(bczs)
countrys = getCountryList(text)
getCountryIPTable(countrys[236])

