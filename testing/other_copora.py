from sentibank import archive
import pickle

# Convert values on a scale to another scale
def convert_values(values, new_min, new_max, old_min, old_max):
    # Calculate the scaling factor
    a = (new_max - new_min) / (old_max - old_min)
    # Calculate the shifting factor
    b = new_min - a * old_min

    # Initialize list
    new_values = []
    for value in values:
        # Apply the linear transformation to each value
        new_value = a * value + b
        # Add new value to list
        new_values.append(round(new_value))
    
    # Return list of new values
    return new_values

if __name__ == "__main__":
    # Load the VADER data from 2014
    load = archive.load()
    vader = load.origin("VADER_v2014")

    # Grab the words and sentiment ratings
    train_x = []
    train_y = []
    for i in range(7517):
        word = vader.loc[i]["SentimentExpression"]
        polarity = vader.loc[i]["mean"]
        train_x.append(str(word))
        train_y.append(float(polarity))

    # Convert ratings from a (-4, 4) scale to a (1, 5) scale
    train_y = convert_values(train_y, 1, 5, -4, 4)

    vader_data = [train_x, train_y]

    # Dump data with pickle
    picklefile = open("data/vaderPickle", "ab")
    pickle.dump(vader_data, picklefile)
    picklefile.close()

    # Load the AFINN data from 2015
    load = archive.load()
    afinn = load.origin("AFINN_v2015")

    # Grab the words and sentiment ratings
    train_x = []
    train_y = []
    for i in range(3382):
        word = afinn.loc[i]["lexicon"]
        polarity = afinn.loc[i]["score"]
        train_x.append(str(word))
        train_y.append(float(polarity))

    # Convert ratings from a (-5, 5) scale to a (1, 5) scale
    train_y = convert_values(train_y, 1, 5, -5, 5)

    afinn_data = [train_x, train_y]

    # Dump data with pickle
    picklefile = open("data/afinnPickle", "ab")
    pickle.dump(afinn_data, picklefile)
    picklefile.close()
