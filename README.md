# Quotes Scraper and Sentiment Analyzer

This program demonstrates a simple web scraping and sentiment analysis workflow. It scrapes quotes from a website, saves them to a text file, and then performs sentiment analysis.

The analyzer shows the analysis of the quotes in the form of a bar graph where the x-axis represents the statements' polarity and the y-axis represents their frequency.

**Polarity:** Polarity lies between [-1,1], -1 defines a negative sentiment and 1 defines a positive sentiment. Negative words reverse the polarity. To know more about Polarity, [click](https://anvilproject.org/guides/content/creating-links) on the link.

## Prerequisites

- Python 3
- Required Python packages: `requests`, `beautifulsoup4`, `pandas`, `matplotlib`, `textblob`

Install the required packages using the following command:

for UNIX-based OS
```bash
    pip3 install -r requirements.txt
```

for Windows/Venv
```bash
    pip install -r requirements.txt
```

## How to run the application
To run the application use the following command in the terminal,

```bash
    git clone https://github.com/HarshvardhanJ/web-quotes-scraper.git
    cd /web-quotes-scraper
```

for UNIX-based OS:
```bash 
    python3 application.py
```

for Windows/Venv:
```bash
    python application.py
```
