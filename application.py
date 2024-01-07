# tui.py

from web_scraper import scrape_quotes, scrape
from data_analysis import analyze

def main():
    """
    Main function to run the Quotes Scraper.
    """
    print("Welcome to the Quotes Scraper!")

    # Scrape quotes
    input("Press Enter to scrape quotes...")
    scrape()
    print("Quotes have been scraped and saved to 'quotes.txt'!")

    # Analyze quotes
    input("Press Enter to analyze quotes...")
    analyze()

if __name__ == "__main__":
    main()
