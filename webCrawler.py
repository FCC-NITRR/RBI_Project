import requests
from bs4 import BeautifulSoup as bs

HOME_URL = "https://www.rbi.org.in/"


def crawler1(url):

    response = requests.get(url)

    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')

        availableLinks = soup.find_all('a', {'class' : 'link2'})
        allLinks = []
        for link in availableLinks:
            href = link['href']
            if '#' not in href:
                if 'http' in href:
                    allLinks.append(href)
                elif '..' in href:
                    href = HOME_URL + href[3:]
                    allLinks.append(href)
                else:
                    if '?' in url and '?' in href:
                        i1 = url.index('?')
                        i2 = href.index('?')
                        href = url[:i1+1]+href[i2+1:]
                        allLinks.append(href)

        
        for x in allLinks:
            scrapeData(x)


    else:
        print("Failed")

def scrapeData(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        soup.prettify()
        heading = soup.find_all('b')
        data = soup.find_all('p')
        allData = ""
        headingData = ""

        for content in heading:
            headingData += " " + content.get_text()

        for content in data:
            allData += " " + content.get_text()
        print(headingData)
        print(allData)
        print()

        

    else:
        print("Failed")


def homePageCrawler(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')

        allLinks = soup.find_all('a')
        directDataLinks = []
        otherLinks = []

        for link in allLinks:
            if link.has_attr('href'):
                href = link['href']

                if '..' in href:
                    otherLinks.append(href)
                
                if len(href)>5 and 'https' in href and 'rbi' in href:
                    directDataLinks.append(href)

        for x in directDataLinks:
            scrapeData(x)

        for x in otherLinks:
            x = HOME_URL + x[3:]
            crawler1(x)

        
    else:
        print("Failed")


    

homePageCrawler(HOME_URL)
