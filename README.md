# Web Scraping with Python

This Python script uses BeautifulSoup, requests, and csv to scrape web page data and write it to a CSV file.

## How it Works

1. The script opens (or creates if it doesn't exist) a CSV file named 'output.csv' in write mode.
2. It writes a row with the headers 'URL' and 'Heading' to the CSV file.
3. It opens another CSV file named 'input.csv' in read mode. This file is expected to contain URLs that the script will scrape data from.
4. For each URL, it sends a GET request to the URL and gets the HTML content of the page.
5. It creates a BeautifulSoup object with the HTML content, using 'lxml' as the parser.
6. It finds all 'h1' elements (headings) in the HTML content.
7. For each heading, it writes a row with the URL and the heading text to 'output.csv'.

## Requirements

- Python 3
- BeautifulSoup
- requests
- csv

