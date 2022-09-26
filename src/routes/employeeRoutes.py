from flask import Blueprint, flash, redirect, render_template, request

from ..entities.user import User
from ..entities.employee import Employee
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
    else:
      legend = ["User id", "Status"]

    data = EmployeeModels.workbench(option)
    return render_template("workbench.html", legend = legend, data = data, option = option)
  return render_template("workbench.html", option = None, data = None)

@main.route("/create/<option>/<id>", methods=["GET", "POST"])
def create(option, id):
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

    EmployeeModels.edit(option, legend, id)
    flash(f"{option.capitalize()} {id} successfully edited.")  
    return redirect("/workbench")

  return render_template("edit.html", option = option, id = id)

@main.route("/delete/<option><id>")
def delete(option, id):
  EmployeeModels.delete(option, id)
  flash(f"{option.capitalize()} {id} successfully deleted.")
  return redirect("/workbench")
