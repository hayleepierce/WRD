import csv
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import CountVectorizer
from articles import articles
import pickle

""" Training the Gaussian Naive Bayes model using the given data. """

def vectorization(train_x, train_y, vectorizer):
    # Vectorize the training data
    train_x = vectorizer.fit_transform(train_x)

    # Convert lists to arrays
    train_x, train_y = train_x.toarray(), np.array(train_y)

    return train_x, train_y

# Get the training data from the given file
# train_x: words, train_y: labels
def get_train_set(filename):
    # Initialize lists
    train_x = []
    train_y = []
    # Open and read the given file
    with open(filename, "r") as file:
        csvfile = csv.reader(file)
        # Iterate through the lines in the file
        for line in csvfile:
            # Add the data in the necessary format
            if "sentiment rating" not in line:
                train_x.append(line[1])
                train_y.append(round(float(line[2])))
    
    train_x, train_y = vectorization(train_x, train_y, vectorizer)
    # Return the training data
    return train_x, train_y

# Predict the sentiment rating of the given articles
def predict_article_sentiment(articles, model, vectorizer):
    for article in articles:
        # Transform the article into the necessary format
        vectorized_article = vectorizer.transform(article).toarray()
        # Predict the sentiment rating of the article
        prediction = model.predict(vectorized_article).tolist()
        total = 0
        for pred in prediction:
            total += pred
        mean = (total / len(prediction))
        print(f"Predicted sentiment rating for article: {mean}")

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

""" Train using WRD data. """

print("Training with WRD...")

# Get the training data
train_x, train_y = get_train_set("data/WRD_updated.csv")

# Initialize the Gaussian Naive Bayes model
model = GaussianNB()

# Fit the model with the training data
model.fit(train_x, train_y)

predict_article_sentiment(articles, model, vectorizer)

""" Train using AFINN data. """

print("Training with AFINN...")

# Load data from pickle file
picklefile = open("data/afinnPickle", "rb")
afinn_data = pickle.load(picklefile)
picklefile.close()

# Vectorize the AFINN data
train_x, train_y = vectorization(afinn_data[0], afinn_data[1], vectorizer)

# Initialize the Gaussian Naive Bayes model
model = GaussianNB()

# Fit the model with the training data
model.fit(train_x, train_y)

predict_article_sentiment(articles, model, vectorizer)

""" Train using SenticNet data. """

print("Training with SenticNet...")

# Load data from pickle file
picklefile = open("data/senticnetPickle", "rb")
senticnet_data = pickle.load(picklefile)
picklefile.close()

# Vectorize the SenticNet data
train_x, train_y = vectorization(senticnet_data[0], senticnet_data[1], vectorizer)

# Initialize the Gaussian Naive Bayes model
model = GaussianNB()

# Fit the model with the training data
model.fit(train_x, train_y)

predict_article_sentiment(articles, model, vectorizer)
