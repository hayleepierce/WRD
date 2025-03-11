import csv
from nltk import NaiveBayesClassifier

""" Training the Naive Bayes Classifier using the given data. """

def get_train_set(filename):
    # Initialize list
    train_set = []
    # Open and read the given file
    with open(filename, "r") as file:
        csvfile = csv.reader(file)
        # Iterate through the lines in the file
        for line in csvfile:
            # Add the data in the necessary format
            # TODO: Reconfigure the labels? Make similar to other datasets?
            train_set.append(({f'contains({line[1]})': True}, line[2]))
    # Remove the labels from the data
    train_set = train_set[1:]
    return train_set

train_set = get_train_set("data/WRD_updated.csv")

model = NaiveBayesClassifier.train(train_set)

print(model.classify({'contains(admiration)': True}))
