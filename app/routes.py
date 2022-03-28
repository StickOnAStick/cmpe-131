from app import myobj
#from app.login import LoginForm
from flask import render_template, flash

@myobj.route('/')
def home(name, city_names):
    name = "Nicholas"
    city_names = ["Paris", "London", "Rome", "Thaiti"]
    return render_template("Home.html" , name = name , city_names = city_names)

