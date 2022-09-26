from flask import Blueprint, flash, redirect, render_template, request

from ..entities.user import User
from ..models.userModels import UserModels
from ..utils.mail import sendMessage

main = Blueprint("userRoutes", __name__)

@main.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form["email"]
    password = request.form["password"]

    user = User(None,
                None,
                None, 
                email, 
                None, 
                password,
                None)

    loggedUser = UserModels.login(user)
    if (loggedUser != None and loggedUser.password):
      return redirect("/home/client")
    flash("Credentials don't match...")
  return render_template("login.html")

@main.route("/forgotPassword", methods=["GET", "POST"])
def forgotPassword():
  if request.method == "POST":
    email = request.form["email"]
    password = User.generatePassword()
    securityKey = (request.form["key1"] + request.form["key2"] + request.form["key3"])

    user = User(None,
                None,
                None, 
                email, 
                None, 
                password,
                securityKey)

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
    password = User.generatePassword()
    securityKey = (request.form["key1"] + request.form["key2"] + request.form["key3"])

    user = User(None,
                firstName,
                lastName, 
                email, 
                username, 
                password,
                securityKey)

    UserModels.registration(user)
    sendMessage(email, password)
    flash("Please check your email...")
    return redirect("/login")
  return render_template("registration.html")