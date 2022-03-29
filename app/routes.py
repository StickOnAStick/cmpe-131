from app import myobj
#from app.login import LoginForm
from flask import Flask, render_template, request, flash
import re

name = "Nicholas"
city_names = ["Paris", "London", "Rome", "Thaiti"]

@myobj.route('/', methods = ['GET' , 'POST'])
def home():
        if request.method == 'POST':
                city = request.form['input']
                flash()
                return render_template("Home.html" , name = name , city_names = city_names)
        else:
                return render_template("Home.html" , name = name , city_names = city_names)
    


    

