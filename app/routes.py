from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template('main.html', this_identifier=0)

@app.route("/portfolio")
def portfolio():
    return render_template('images.html', this_identifier=1, directory='portfolio', length=25)

@app.route("/patterns")
def patterns():
    return render_template('images.html', this_identifier=2, directory='patterns', length=8)

@app.route("/money")
def about():
    return render_template('money.html', this_identifier=3)
