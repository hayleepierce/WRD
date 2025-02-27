from pymongo import MongoClient
import os
import json
import csv
import pandas as pd
from dotenv_vault import load_dotenv
from emotion_entries import emotion_entries
from noun_adjective_entries import noun_entries, adjective_entries

""" Load original ratings. """

# wrd_entries = []
# for entry in emotion_entries:
#     wrd_entries.append(entry)
# for entry in noun_entries:
#     wrd_entries.append(entry)
# for entry in adjective_entries:
#     wrd_entries.append(entry)

# with open("WRD_orgin.json", "w") as file:
#     json.dump(wrd_entries, file, indent=0)
# with open("WRD_orgin.json", "r") as file:
#     pd_data = pd.read_json(file)
# pd_data.to_csv("WRD_orgin.csv")

""" Add entries to MongoDB. """

# load_dotenv()

# connection_str = os.getenv("CONNECTION_STR")
# client = MongoClient(connection_str)

# db = client["WRD"]
# wrd = db.words

# result = wrd.insert_many(emotion_entries)
# result = wrd.insert_many(noun_entries)
# result = wrd.insert_many(adjective_entries)

""" Compare original ratings and updated ratings. """

# Read data from a given csv file
def read_csv(filename):
    # Initialize lists
    ratings = []

    # Open the given file
    with open(f"{filename}", "r") as file:
        # Read the given file
        csvfile = csv.reader(file)
        # Iterate through the lines in the file
        for line in csvfile:
            # Remove & save the last item each line
            y = line.pop(2)
            if y is not None and y != "sentiment rating":
                # Add the saved item to the all_y_trues list as floats
                ratings.append(float(y))
    return ratings


orgin_ratings = read_csv("data/WRD_orgin.csv")
updated_ratings = read_csv("data/WRD_updated.csv")

# Find the difference
for orgin, updated in zip(orgin_ratings, updated_ratings):
    difference = updated - orgin