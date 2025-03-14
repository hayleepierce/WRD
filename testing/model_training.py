import csv
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import CountVectorizer
from articles import arts as articles

""" Training the Naive Bayes Classifier using the given data. """

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
            # TODO: Reconfigure the labels? Make similar to other datasets?
            if "sentiment rating" not in line:
                train_x.append(line[1])
                train_y.append(int(float(line[2])))

    # Vectorize the training data
    train_x = vectorizer.fit_transform(train_x)

    # Convert lists to arrays
    train_x, train_y = train_x.toarray(), np.array(train_y)
    
    # Return the training data
    return train_x, train_y

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Get the training data
train_x, train_y = get_train_set("data/WRD_updated.csv")

# Initialize the Gaussian Naive Bayes model
model = GaussianNB()

# Fit the model with the training data
model.fit(train_x, train_y)

# TODO: Predict articles
# predictions = model.predict(vectorizer.transform([TODO]).toarray())

# print(predictions)