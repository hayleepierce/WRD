import csv
from matplotlib import pyplot as plt

""" Compare original ratings and updated ratings. """

def read_csv(orgin_filename, updated_filename):
    # Initialize lists to store ratings
    orgin_ratings = []
    updated_ratings = []

    # Open the original ratings CSV file
    with open(f"{orgin_filename}", "r") as o_file:
        o_csvfile = csv.reader(o_file)
        # Iterate through each line in the original ratings CSV
        for o_line in o_csvfile:
            # Open the updated ratings CSV file
            with open(f"{updated_filename}", "r") as u_file:
                u_csvfile = csv.reader(u_file)
                # Iterate through each line in the updated ratings CSV
                for u_line in u_csvfile:
                    # If words are the same and not a header
                    if o_line[1] == u_line[1] and o_line[2] != "sentiment rating" and u_line[2] != "sentiment rating":
                        # Append the ratings to the respective lists
                        orgin_ratings.append(float(o_line[2]))
                        updated_ratings.append(float(u_line[2]))
    # Return the ratings
    return orgin_ratings, updated_ratings

orgin_ratings, updated_ratings = read_csv("data/WRD_orgin.csv", "data/WRD_updated.csv")

# Find the difference
differences = []
for orgin, updated in zip(orgin_ratings, updated_ratings):
    difference = updated - orgin
    differences.append(abs(difference))

dif_vals = list(set(differences))
dif_vals.sort()
for val in dif_vals:
    print(f"{val}: {differences.count(val)}")
