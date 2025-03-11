import csv

""" Compare original ratings and updated ratings. """

# Read data from a given csv file
def read_csv(filename):
    # Initialize list
    ratings = []

    # Open the given file
    with open(f"{filename}", "r") as file:
        # Read the given file
        csvfile = csv.reader(file)
        # Iterate through the lines in the file
        for line in csvfile:
            # Remove & save the sentiment value
            y = line.pop(2)
            if y is not None and y != "sentiment rating":
                # Convert value to float, add to list
                ratings.append(float(y))
    return ratings

orgin_ratings = read_csv("data/WRD_orgin.csv")
updated_ratings = read_csv("data/WRD_updated.csv")

# Find the difference
for orgin, updated in zip(orgin_ratings, updated_ratings):
    difference = updated - orgin