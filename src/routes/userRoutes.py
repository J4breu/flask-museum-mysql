from logging import LoggerAdapter
from flask import Blueprint, flash, redirect, render_template, request

from ..entities.user import User
from ..models.userModels import UserModels

main = Blueprint('userRoutes', __name__)

@main.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    user = User(0, 0, 0, request.form['email'], 0, request.form['password'])
    logged_user = UserModels.login(user)
    if logged_user != None:
      return redirect('/home')
    else:
      flash('User not found...')
  return render_template('login.html')

@main.route('/registration', methods=['GET', 'POST'])
def registration():
  if request.method == "POST":
    firstName = request.form["first-name"]
    lastName = request.form["last-name"]
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]

    user = User(0,
                firstName,
                lastName, 
                email, 
                username, 
                password)

    UserModels.registration(user)
    return redirect('/home')
  return render_template('registration.html')
