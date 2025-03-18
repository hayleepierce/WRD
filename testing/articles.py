
import os
from string import punctuation
from nltk.corpus import stopwords
# from nltk.sentiment.vader import SentimentIntensityAnalyzer

""" Clean the text data (articles). """

stop_words = set(stopwords.words('english'))

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
            # Split the paragraph into words
            words = paragraph.split(" ")
            # Iterate through the words in the paragraph
            for word in words:
                # Convert to lowercase
                word = word.lower()
                # Remove punctuation
                for i in punctuation:
                    word = word.replace(i, "")
                # Remove new line characters
                word = word.replace("\n", "")
                # Only add the word if it is not empty and not a stop word
                if word != "" and word not in stop_words:
                    article.append(word)
    # Add the cleaned article to the list of articles
    articles.append(article)
    
""" Find the sentiment rating of each article. """

# Initialize sentiment analyzer (VADER)
# sia = SentimentIntensityAnalyzer()

# rating = 0
# art = ""
# for article in articles:
#     for paragraph in article:
#         art += paragraph
#     sia_scores = sia.polarity_scores(art)
#     print(sia_scores)
    #     sia_scores = sia.polarity_scores(paragraph)
    #     sia_score = sia_scores["compound"]
    #     if sia_score <= -0.5:
    #         n_rating = 1
    #     elif sia_score > -0.5 and sia_score < 0:
    #         n_rating = 2
    #     elif sia_score == 0:
    #         n_rating = 3
    #     elif sia_score < 0.5 and sia_score > 0:
    #         n_rating = 4
    #     elif sia_score >= 0.5:
    #         n_rating = 5
    #     rating = (rating + n_rating) / 2
    # print(round(rating, 2))
