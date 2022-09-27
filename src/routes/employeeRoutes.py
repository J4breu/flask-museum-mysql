from flask import Blueprint, flash, redirect, render_template, request

from ..entities.art import Art
from ..entities.employee import Employee
from ..entities.user import User
from ..models.employeeModels import EmployeeModels

main = Blueprint("employeeRoutes", __name__)

@main.route("/workbench", methods=["GET", "POST"])
def workbench():
  if request.method == "POST":
    option = request.form["option"]

    if option == "user":
      legend = ["Id",
                "First name",
                "Last name",
                "Email",
                "Username",
                "Password",
                "Security key"]

    if option == "employee":
      legend = ["User id", "Status"]

    if option == "art":
      legend = ["Id",
                "Title",
                "Image link",
                "Autor",
                "Price"]

    data = EmployeeModels.workbench(option)
    return render_template("workbench.html", legend = legend, data = data, option = option)
  return render_template("workbench.html", option = None, data = None)

@main.route("/create/<option>", methods=["GET", "POST"])
def create(option):
  if request.method == "POST":

    if option == "user":
      legend = User(
        None,
        request.form["firstName"],
        request.form["lastName"],
        request.form["email"],
        request.form["username"],
        request.form["password"],
        request.form["key1"] + request.form["key2"] + request.form["key3"])

    if option == "employee":
      legend = Employee(
        request.form["userId"],
        request.form["status"])

    if option == "art":
      legend = Art(
        request.form["title"],
        request.form["imageLink"],
        request.form["gender"],
      )

    EmployeeModels.create(option, legend)
    flash(f"{option.capitalize()} successfully created.")  
    return redirect("/workbench")

  return render_template("create.html", option = option)

@main.route("/edit/<option><id>", methods=["GET", "POST"])
def edit(option, id):
  if request.method == "POST":
    if option == "user":
      legend = User(
        request.form["id"],
        request.form["firstName"],
        request.form["lastName"],
        request.form["email"],
        request.form["username"],
        request.form["password"],
        request.form["key1"] + request.form["key2"] + request.form["key3"])

    if option == "employee":
      legend = Employee(
        request.form["userId"],
        request.form["status"])

    if option == "art":
      legend = Art(
        request.form["id"],
        request.form["title"],
        request.form["imageLink"],
        request.form["gender"],
      )

    EmployeeModels.edit(option, legend, id)
    flash(f"{option.capitalize()} {id} successfully edited.")  
    return redirect("/workbench")

  return render_template("edit.html", option = option, id = id)

@main.route("/delete/<option><id>")
def delete(option, id):
  EmployeeModels.delete(option, id)
  flash(f"{option.capitalize()} {id} successfully deleted.")
  return redirect("/workbench")
