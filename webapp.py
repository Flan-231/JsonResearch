from flask import Flask, request, Markup, render_template, flash
from datetime import datetime

import os
import json

app = Flask(__name__)

@app.route('/')
def render_about():
    return render_template('home.html')
    
@app.route("/p1")
def render_page1():
    game = request.args ['game']
    return render_template('page1.html', options = get_game_options(), )
    
def get_game_options():
    listOfgames = []
    with open ('video_games.json') as Videogames_data:
        game = json.load(Videogames_data)
    for game in Title:
        if not (game ["Title"] in listOfgames):
            listOfgames.append(game["Title"])
    options = ""
    for s in listOfgames:
        options = options + Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options 

def Rating_by_game (game):
    with open('video_games.json') as Videogames_data:
        game = json.load(Vidoogames_data)
    

@app.route("/p2")
def render_page2():
    return render_template('page2.html')
    
def get_release_date():
    with open ('video_games.json') as Videogames_data:
    game= json.load(Video_games_data)
    

if __name__ == '__main__':
    app.run(debug=False) # change to False when running in production
