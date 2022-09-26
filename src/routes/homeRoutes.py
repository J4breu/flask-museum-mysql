from flask import Blueprint, redirect, render_template

main = Blueprint("homeRoutes", __name__)

@main.route('/')
def index():
  return redirect("/home/visitor")

@main.route("/home/<type>")
def home(type):
  return render_template("home.html", data = type)