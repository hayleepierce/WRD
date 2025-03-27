import csv
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import CountVectorizer
from articles import source_articles, topic_articles
import pickle

""" Training the Gaussian Naive Bayes model using the given data. """

def calculate_percentage(value, total):
    percentage = round((value / total) * 100)
    return percentage

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
        # Find mean of predictions
        total = 0
        for pred in prediction:
            total += pred
        mean = (total / len(prediction))
        # Print mean prediction
        print(f"Predicted sentiment rating for article {articles.index(article) + 1}: {round(mean, 2)}")
        # Print individual prediction totals
        print(f"1: {calculate_percentage(prediction.count(1), len(prediction))}%", 
              f"2: {calculate_percentage(prediction.count(2), len(prediction))}%",
              f"3: {calculate_percentage(prediction.count(3), len(prediction))}%",
              f"4: {calculate_percentage(prediction.count(4), len(prediction))}%",
              f"5: {calculate_percentage(prediction.count(5), len(prediction))}%")

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

print("Source Articles")
predict_article_sentiment(source_articles, model, vectorizer)
print("Topic Articles")
predict_article_sentiment(topic_articles, model, vectorizer)


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

print("Source Articles")
predict_article_sentiment(source_articles, model, vectorizer)
print("Topic Articles")
predict_article_sentiment(topic_articles, model, vectorizer)

""" Train using VADER data. """

print("Training with VADER...")

# Load data from pickle file
picklefile = open("data/vaderPickle", "rb")
vader_data = pickle.load(picklefile)
picklefile.close()

# Vectorize the VADER data
train_x, train_y = vectorization(vader_data[0], vader_data[1], vectorizer)

# Initialize the Gaussian Naive Bayes model
model = GaussianNB()

# Fit the model with the training data
model.fit(train_x, train_y)

print("Source Articles")
predict_article_sentiment(source_articles, model, vectorizer)
print("Topic Articles")
predict_article_sentiment(topic_articles, model, vectorizer)
