from flask import Flask, render_template, request
from dotenv_vault import load_dotenv
from pymongo import MongoClient
import os
import ast
import random

app = Flask(__name__)
load_dotenv()

#connecting to my MongoDB cluster
connection_str = os.getenv("CONNECTION_STR")
client = MongoClient(connection_str)

# accessing the WRD database
db = client["WRD"]
wrd = db.words
# WRD database as a list
database = wrd.find({}, {"_id": False}).to_list()

# used to update the rating of a word
def update_rating(word_data: dict, user_rating: int):
    new_rating = round((word_data["sentiment rating"] + user_rating)/2, 2)
    wrd.find_one_and_update(word_data, {'$set': {"sentiment rating": new_rating}})


"""""
main page: shows random word with slider to rate, 
button to catalog of words, 
button to add new word
"""
@app.route("/", methods=["GET", "POST"])
def index():
    # Update rating during POST requests
    if request.method == "POST":
        user_rating = int(request.form["user_rating"])
        word_data = ast.literal_eval(request.form["word_data"])
        update_rating(word_data, user_rating)
    # find random word in database
    result = random.choice(database)
    return render_template("main.html", word_data=result)

"""
Results of the users search
"""
@app.route("/search-results", methods=["GET"])
def search_results():
    search = request.args.get("search")
    results = []
    if "tag:" in search:
        search = search.replace("tag:", "")
        for entry in database:
            if search in entry["tags"]:
                results.append(entry)
        return render_template("search_results.html", search_results=results)
    else:
        for entry in database:
            if search in entry["word"]:
                results.append(entry)
        return render_template("search_results.html", search_results=results)

"""
Allows user to rate a word from their search results
"""
@app.route("/search-results/<word>", methods=["GET"])
def search_results_word(word):
    for entry in database:
        if entry["word"] == word:
            return render_template("main.html", word_data=entry)
            
"""
Catalog of words in database, 
alphabetical and/or by tags?,
can click on each word
"""
# @app.route("/catalog")
# def catalog():

"""
word display,
show slider(s) to rate,
and definiton?
"""
# @app.route("/catalog/<word>")
# def chosen_word():

"""
adding new word page,
inputs: word name,
tags [WIP],
slider
"""
# @app.route("/add-new-word")
# def add_new_word():
#     return render_template('new_word.html')

"""
adds new word to database, 
displays it
"""
# @app.route("/new-word")
# def new_word():
#     word = request.args.get("word")
#     first_rating = request.args.get("first_rating")
#     tags = request.args.get("tags")
#     word_data = {
#         "word": word,
#         "sentiment rating" : first_rating,
#         "tags": tags
#     }

#     #accessing the words collections within the WRD database
#     result = wrd.insert_one(word_data)
#     return result