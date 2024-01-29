from bs4 import BeautifulSoup
import requests
import csv
with open('output.csv', 'w', encoding='utf-8')as file:         #it creates a csv file
    writer=csv.writer(file)                                    #it writes in the csv file
    writer.writerow(['URL','Heading'])                         #it writes the heading of the columns
    with open('input.csv', 'r', encoding='utf-8')as file:      #it opens the csv file
        reader=csv.reader(file)                                #it reads the csv file                           
        for row in reader:                                     #it reads the rows of the csv file                 
            source=requests.get(row[0]).text                   #it returns the html file
            soup=BeautifulSoup(source, 'lxml')                 #it returns the html file in a readable format
            for heading in soup.find_all('h1'):
                print(heading.text)
                writer.writerow([row[0],heading.text])         #it writes the url and heading in the csv file
                print()      
