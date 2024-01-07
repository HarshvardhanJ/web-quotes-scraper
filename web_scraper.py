# web_scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    """
    Scrapes quotes from a given URL.

    Parameters:
    - url (str): The URL of the website to scrape.

    Returns:
    - list: List of scraped quotes.
    """
    # Make a GET request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract quotes from the HTML
    quotes = []
    for quote_elem in soup.find_all('div', class_='quote'):
        quote = quote_elem.find('span', class_='text').text
        quotes.append(quote)
    
    return quotes

def scrape():
    """
    Scrapes quotes from 'https://quotes.toscrape.com' and saves them to 'quotes.txt'.
    """
    url = 'https://quotes.toscrape.com'
    quotes = scrape_quotes(url)

    # Save quotes to a text file
    with open('quotes.txt', 'w', encoding='utf-8') as file:
        for quote in quotes:
            file.write(quote + '\n')
