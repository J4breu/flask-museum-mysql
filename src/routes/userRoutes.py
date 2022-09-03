from flask import Blueprint, flash, redirect, render_template, request

from ..entities.user import User
from ..models.userModels import UserModels

main = Blueprint('userRoutes', __name__)

@main.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    user = User(0, 0, 0, request.form['text'], 0, request.form['password'])
    loggedUser = UserModels.login(user)
    if loggedUser != None:
      return redirect('/home')
    else:
      flash('User not found...')
  return render_template('login.html')

@main.route('/registration', methods=['GET', 'POST'])
def registration():
  if request.method == "POST":
    firstName = request.form["firstName"]
    lastName = request.form["lastName"]
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