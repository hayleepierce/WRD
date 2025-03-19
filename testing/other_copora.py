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
    # Load the SenticNet data from 2022
    load = archive.load()
    senticnet = load.origin("SenticNet_v2022")

    # Grab the words and sentiment ratings
    train_x = []
    train_y = []
    for i in range(300000):
        word = senticnet.loc[i]["CONCEPT"]
        polarity = senticnet.loc[i]["POLARITY INTENSITY"]
        train_x.append(str(word))
        train_y.append(float(polarity))

    # Convert ratings from a (-1, 1) scale to a (1, 5) scale
    train_y = convert_values(train_y, 1, 5, -1, 1)

    senticnet_data = [train_x, train_y]

    # Dump data with pickle
    picklefile = open("data/senticnetPickle", "ab")
    pickle.dump(senticnet_data, picklefile)
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
