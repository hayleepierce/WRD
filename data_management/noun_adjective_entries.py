from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer


with open("data/.txt", "r") as txt:
    txt = TextBlob(txt.read())

tags = txt.tags

adjective = ["JJ", "JJR", "JJS"]

n = []
a = []

for word in tags:
    if word[1] == "NN" and word not in n:
        n.append(word)
    elif word[1] in adjective and word not in a:
        a.append(word)

sia = SentimentIntensityAnalyzer()

def rate_entries(words: list[tuple], tag: str) -> list:
    new_entries = []
    for word in words:
        sia_scores = sia.polarity_scores(word[0])
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
        new_entries.append(
            {
                "word": word[0].lower(), 
                "sentiment rating": rating, 
                "tags": [tag]
            }
        )
    
    return new_entries

noun_entries = rate_entries(n, "noun")
adjective_entries = rate_entries(a, "adjective")
