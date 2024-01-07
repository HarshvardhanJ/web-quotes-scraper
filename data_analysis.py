# data_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

def perform_sentiment_analysis(text):
    """
    Performs sentiment analysis on a given text.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    - float: Sentiment polarity score.
    """
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def analyze():
    """
    Reads quotes from 'quotes.txt', performs sentiment analysis, and visualizes the sentiment distribution.
    """
    # Read quotes from the text file into a DataFrame
    quotes_df = pd.read_csv('quotes.txt', header=None, names=['Quote'])
    
    # Apply sentiment analysis to each quote
    quotes_df['Sentiment'] = quotes_df['Quote'].apply(perform_sentiment_analysis)

    # Visualize sentiment distribution using a histogram
    plt.hist(quotes_df['Sentiment'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Sentiment Distribution of Quotes')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Frequency')
    plt.show()
