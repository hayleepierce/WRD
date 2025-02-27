import csv
from nltk.sentiment import SentimentIntensityAnalyzer

wrd_list = []

with open("data/emotionlist.csv", "r") as emot_list:
    reader = csv.reader(emot_list)
    for row in reader:
        if "â€‹" in row[0]:
            row[0] = row[0].replace("â€‹", "")
        wrd_list.append(row[0])

emotion_entries = []

sia = SentimentIntensityAnalyzer()

for word in wrd_list:
    sia_scores = sia.polarity_scores(word)
    sia_score = sia_scores["compound"]
    if sia_score <= -0.5:
        rating = 1
    elif sia_score > -0.5 and sia_score < 0:
        rating = 2
    elif sia_score == 0:
        rating = 3
    elif sia_score < 0.5 and sia_score > 0:
        rating = 4
    elif sia_score >= 0.5:
        rating = 5
    emotion_entries.append(
        {
            "word": word.lower(), 
            "sentiment rating": rating, 
            "tags": ["emotion"]
        }
    )