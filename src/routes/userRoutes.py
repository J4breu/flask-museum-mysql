from flask import Blueprint, flash, redirect, render_template, request
from flask_login import login_user, logout_user, login_required, current_user

from ..entities.user import User
from ..models.userModels import UserModels
from ..utils.password import generatePassword
from ..utils.mail import sendMessage

main = Blueprint("userRoutes", __name__)

@main.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form["email"]
    password = request.form["password"]
    remember = True if request.form.get("remember") else False

    user = User(None, None, None, email, None, password, None)

    loggedUser = UserModels.login(user)
    if (loggedUser != None and loggedUser.password):
      login_user(loggedUser, remember=remember)
      return redirect("/home")
    flash("Credentials don't match...")
  return render_template("login.html")

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/home")

@main.route("/forgotPassword", methods=["GET", "POST"])
def forgotPassword():
  if request.method == "POST":
    email = request.form["email"]
    password = generatePassword()
    securityKey = (request.form["key1"] + request.form["key2"] + request.form["key3"])

    user = User(None, None, None, email, None, password, securityKey)

    loggedUser = UserModels.forgotPassword(user)
    if (loggedUser != None):
      sendMessage(email, password)
      flash("Please check your email...")
      return redirect("/login")
    flash("Credentials don't match...")
  return render_template("forgotPassword.html")

@main.route("/registration", methods=["GET", "POST"])
def registration():
  if request.method == "POST":
    firstName = request.form["firstName"]
    lastName = request.form["lastName"]
    email = request.form["email"]
    username = request.form["username"]
    password = generatePassword()
    securityKey = (request.form["key1"] + request.form["key2"] + request.form["key3"])

    if (UserModels.search("email", email) or UserModels.search("username", username)):
      flash("Duplicate credentials (email or username)")
      return redirect("/registration")

    user = User(None, firstName, lastName, email, username, password, securityKey)

    UserModels.registration(user)
    sendMessage(email, password)
    flash("Please check your email...")
    return redirect("/login")
  return render_template("registration.html")