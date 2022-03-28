from re import A
from app import app
#from app.login import LoginForm
from flask import render_template, flash

@app.route('/')
def home():
    name = "Nicholas"
    city_names = ["Paris", "London", "Rome", "Thaiti"]
    return render_template("Home.html" , name=name , city_names=city_names)
