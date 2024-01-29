from bs4 import BeautifulSoup
import requests
source=requests.get('https://timesofindia.indiatimes.com/city/jaipur/sorry-mummy-papa-jee-aspirant-ends-her-life-in-kota-leaves-suicide-note/articleshow/107229508.cms').text
soup=BeautifulSoup(source, 'lxml')
for heading in soup.find_all('h1'):
    print(heading.text)
    print()
for para in soup.find_all('div' , class_='_s30J clearfix'):
    print(para.text)
    print()