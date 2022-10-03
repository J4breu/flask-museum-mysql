from flask import Blueprint, flash, redirect, render_template, request
from flask_login import login_user, logout_user, login_required

from ..entities.user import User
from ..models.userModels import UserModels
from ..models.clientModels import ClientModels
from ..utils.password import generatePassword
from ..utils.mail import sendMessage

main = Blueprint("userRoutes", __name__)

@main.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    user = User(None, None, None, request.form["email"], None, request.form["password"], None)
    remember = True if request.form.get("remember") else False

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
    user = User(
      None,
      None,
      None,
      request.form["email"],
      None,
      generatePassword(6),
      (request.form["key1"] + request.form["key2"] + request.form["key3"])
    )

    loggedUser = UserModels.forgotPassword(user)
    if (loggedUser != None):
      sendMessage(user.email, user.password)
      flash("Please check your email...")
      return redirect("/login")
    flash("Credentials don't match...")
  return render_template("forgotPassword.html")

@main.route("/registration", methods=["GET", "POST"])
def registration():
  if request.method == "POST":
    user = User(
      None,
      request.form["firstName"],
      request.form["lastName"],
      request.form["email"],
      request.form["username"],
      generatePassword(6),
      (request.form["key1"] + request.form["key2"] + request.form["key3"])
    )

    if (UserModels.search("email", user.email) or UserModels.search("username", user.username)):
      flash("Duplicate credentials (email or username)")
      return redirect("/registration")

    UserModels.registration(user)
    ClientModels.new(user.email)
    sendMessage(user.email, user.password)
    flash("Please check your email...")
    return redirect("/login")
  return render_template("registration.html")