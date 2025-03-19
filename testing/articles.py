
import os
from string import punctuation
from nltk.corpus import stopwords

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
