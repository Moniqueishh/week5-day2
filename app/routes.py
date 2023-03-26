
from app import app

from flask import render_template, request, url_for, redirect
from .forms import SignUpForm
from .models import User


@app.route('/')
def homePage():
    return render_template('index.html')

# @app.route('/favoritefive')
# def favoriteFive():
#     favorite = [
#             {
#             "name" : "The 1975"
#             },
#             {
#             "name" : "Hozier"
#             },
#             {
#             "name" : "Jesse Reyez"
#             },
#             {
#             "name" : "Omar Apollo"
#             },
#             {
#             "name" : "Kali Uchis"
#             }
#         ]
#     return render_template("favoritefive.html", favorite=favorite)

@app.route('/login')
def loginPage():
    return render_template('login.html')

@app.route('/register', methods= ["GET", "POST"])
def registerPage():
    form = SignUpForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            user = User(username, email, password)
            user.saveUser()
            return redirect(url_for("loginPage"))
            

    return render_template('register.html', form=form)