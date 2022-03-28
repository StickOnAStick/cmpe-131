from app import myobj
#from app.login import LoginForm
from flask import render_template, flash

name = "Nicholas"
city_names = ["Paris", "London", "Rome", "Thaiti"]

@myobj.route('/')
def home():
    
    return render_template("Home.html" , name = name , city_names = city_names)
    
    

