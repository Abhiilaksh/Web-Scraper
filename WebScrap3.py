from bs4 import BeautifulSoup
import requests
source=requests.get('https://timesofindia.indiatimes.com/india/union-minister-says-caa-will-be-implemented-in-one-week-mamata-banerjee-hits-back/articleshow/107229633.cms').text
soup=BeautifulSoup(source, 'lxml')
for heading in soup.find_all('h1'):
    print(heading.text)
    print()
for para in soup.find_all('div' , class_='_s30J clearfix'):
    print(para.text)
    print()
