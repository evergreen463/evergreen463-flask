# -*- coding: utf-8 -*-
# flask run --host 0.0.0.0 --port 8080 플라스크 실행시킬때
from flask import Flask, render_template, request
import random
import datetime
import requests
from bs4 import BeautifulSoup 

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")
    
@app.route("/takhee")
def hellotak():
    return "Hello, takhee"

@app.route("/lunch")
def lunch():
    lunch_box = ["20층", "김밥카페", "양자강", "바스버거", "시골집"]
    lunch = random.choice(lunch_box)
    return render_template("lunch.html", lunch=lunch, box=lunch_box)

@app.route("/christmas")
def christmas():
    now = datetime.datetime.now()
    christmas = ""
    if now.day == 25 and now.month ==12:
        christmas = "맞아!"
    else:
        christmas = "아니야!"
    return render_template("christmas.html", christmas=christmas)
    
@app.route("/google")
def google():
    return render_template("google.html")

@app.route('/opgg')
def opgg():
    return render_template("opgg.html")
    
@app.route("/opggresult")
def opggresult():
    name = request.args.get('q')
    url = "http://www.op.gg/summoner/userName="+name
    res=requests.get(url)
    result =BeautifulSoup(res.content,'html.parser')
    win=result.select_one('span.wins').text
    lose=result.select_one('span.losses').text
    return render_template("opggresult.html", name=name, win=win, lose=lose)
    
