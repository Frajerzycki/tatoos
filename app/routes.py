from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template('main.html', this_identifier=0)

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html', this_identifier=1)

@app.route("/money")
def about():
    return render_template('money.html', this_identifier=2)
