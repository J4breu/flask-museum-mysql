from flask import Blueprint, redirect, render_template

main = Blueprint("visitorRoutes", __name__)

@main.route('/')
def index():
  return redirect("/home")

@main.route("/home")
def home():
  return render_template("home.html")