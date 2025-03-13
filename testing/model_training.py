import csv
from articles import arts as articles
from nltk import NaiveBayesClassifier

""" Training the Naive Bayes Classifier using the given data. """

def get_train_set(filename):
    # Initialize lists
    words = []
    train_set = []
    # Open and read the given file
    with open(filename, "r") as file:
        csvfile = csv.reader(file)
        # Iterate through the lines in the file
        for line in csvfile:
            # Add the data in the necessary format
            # TODO: Reconfigure the labels? Make similar to other datasets?
            if line[2] != "sentiment rating":
                words.append(f'contains({line[1]})')
                train_set.append(({f'contains({line[1]})': True}, int(float((line[2])))))
    return train_set, words

# Not helpful
def rm_unknowns(words, articles):
    for article in articles:
        art = {}
        for word in article:
            if word in words:
                art.update({f'contains({word})': True})
        article = art

""" Training the Naive Bayes Classifier using the original data. """

train_set, words = get_train_set("data/WRD_orgin.csv")

# Train the Naive Bayes Classifier
orgin = NaiveBayesClassifier.train(train_set)

# Print the most informative features
print(orgin.show_most_informative_features(5))

# Test the classifier
for article in articles:
    print(orgin.classify(article))

""" Training the Naive Bayes Classifier using the updated data. """

train_set, words = get_train_set("data/WRD_updated.csv")

# Train the Naive Bayes Classifier
updated = NaiveBayesClassifier.train(train_set)

# Print the most informative features
print(updated.show_most_informative_features(5))

# Test the classifier
for article in articles:
    print(updated.classify(article))