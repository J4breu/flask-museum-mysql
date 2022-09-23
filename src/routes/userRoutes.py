from flask import Blueprint, flash, redirect, render_template, request

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

    user = User(0,
                0,
                0, 
                email, 
                0, 
                password,
                0)

    loggedUser = UserModels.login(user)
    if (loggedUser != None and loggedUser.password):
      return redirect("/home")
    flash("User not found...")
  return render_template("login.html")

@main.route("/registration", methods=["GET", "POST"])
def registration():
  if request.method == "POST":
    firstName = request.form["firstName"]
    lastName = request.form["lastName"]
    email = request.form["email"]
    username = request.form["username"]
    password = generatePassword()
    securityKey = (request.form["key1"] + request.form["key2"] + request.form["key3"])

    user = User(0,
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