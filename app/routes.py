from app import myobj
#from app.login import LoginForm
from flask import Flask, render_template, request, flash

name = "Nicholas"
city_names = ["Paris", "London", "Rome", "Thaiti"]

@myobj.route('/', methods = ['GET' , 'POST'])
def home():
        if request.method == 'POST':
                city = request.form['input']
                flash(city)
                
        return render_template("home.html" , name = name , city_names = city_names)
    


    

