import requests
import csv
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
                if 'http' in href and 'image' not in href:
                    allLinks.append(href)
                elif '..' in href and 'image' not in href:
                    href = HOME_URL + href[3:]
                    allLinks.append(href)
                else:
                    if '?' in url and '?' in href and 'image' not in href:
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

        write_to_csv(url, headingData, allData)

    else:
        print("Failed")

def write_to_csv(url, headingData, allData):
    with open('data.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['URL', 'Heading', 'Content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if the file is empty, then write header
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'URL': url, 'Heading': headingData, 'Content': allData})

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
            if 'image' not in x:
                scrapeData(x)

        for x in otherLinks:
            x = HOME_URL + x[3:]
            crawler1(x)

        
    else:
        print("Failed")


    

homePageCrawler(HOME_URL)
