
import os
from string import punctuation
from nltk.sentiment.vader import SentimentIntensityAnalyzer

""" Clean the text data (articles). """

# Add to string.punctuation
punctuation += "-â€“”™‘’—–"

# Initialize list for all articles
articles = []

# Iterate through all .txt files
for txt in os.scandir("data/articles"):
    # Initialize list for individual article
    article = []
    with open(txt, "r", encoding="utf-8") as f:
        # Read each line of the .txt file
        paragraphs = f.readlines()
        # Iterate through the lines
        for paragraph in paragraphs:
            # Make all text lowercase
            paragraph = paragraph.lower()
            # Remove newlines
            paragraph = paragraph.replace("\n", "")
            # Remove special characters
            for i in punctuation:
                paragraph = paragraph.replace(i, " ")
            # Remove double spaces
            while "  " in paragraph:
                paragraph = paragraph.replace("  ", " ")
            if paragraph != "":
                # Add the cleaned paragraph to the article list
                article.append(paragraph)
    # Add the article to the articles list
    articles.append(article)

""" Find the sentiment rating of each article. """

# Initialize sentiment analyzer (VADER)
sia = SentimentIntensityAnalyzer()

rating = 0
for article in articles:
    for paragraph in article:
        sia_scores = sia.polarity_scores(paragraph)
        sia_score = sia_scores["compound"]
        if sia_score <= -0.5:
            n_rating = 1
        elif sia_score > -0.5 and sia_score < 0:
            n_rating = 2
        elif sia_score == 0:
            n_rating = 3
        elif sia_score < 0.5 and sia_score > 0:
            n_rating = 4
        elif sia_score >= 0.5:
            n_rating = 5
        rating = (rating + n_rating) / 2
    print(round(rating, 2))
