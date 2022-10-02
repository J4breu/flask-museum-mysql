from flask import Blueprint, flash, redirect, render_template, request
from flask_login import login_required, current_user

from ..entities.user import User
from ..entities.employee import Employee
from ..models.employeeModels import EmployeeModels

main = Blueprint("employeeRoutes", __name__)

@main.route("/create/<option>", methods=["GET", "POST"])
@login_required
def create(option):
  if (current_user.status == None):
      return redirect("/Create")

  if request.method == "POST":

    if option == "user":
      data = User(
        None,
        request.form["firstName"],
        request.form["lastName"],
        request.form["email"],
        request.form["username"],
        request.form["password"],
        request.form["key1"] + request.form["key2"] + request.form["key3"]
      )

    if option == "employee":
      data = Employee(request.form["userId"], request.form["status"])

    EmployeeModels.create(option, data)
    flash(f"{option.capitalize()} successfully created.")  
    return redirect("/workbench")
  return render_template("create.html", option = option)

@main.route("/delete/<option><id>")
@login_required
def delete(option, id):
  if (current_user.status == None):
      return redirect("/Delete")

  EmployeeModels.delete(option, id)
  flash(f"{option.capitalize()} {id} successfully deleted.")
  return redirect("/workbench")

@main.route("/edit/<option><id>", methods=["GET", "POST"])
@login_required
def edit(option, id):
  if (current_user.status == None):
      return redirect("/Edit")

  if request.method == "POST":
    if option == "user":
      data = User(
        request.form["id"],
        request.form["firstName"],
        request.form["lastName"],
        request.form["email"],
        request.form["username"],
        request.form["password"],
        request.form["key1"] + request.form["key2"] + request.form["key3"]
      )

    if option == "employee":
      data = Employee(request.form["userId"], request.form["status"])

    EmployeeModels.update(option, data, id)
    flash(f"{option.capitalize()} {id} successfully edited.")  
    return redirect("/workbench")

  data = EmployeeModels.edit(option, id)
  return render_template("edit.html", option = option, data = data)

@main.route("/workbench", methods=["GET", "POST"])
@login_required
def workbench():
  if (current_user.status == None):
    return redirect("/Workbench")

  if request.method == "POST":
    option = request.form["option"]

    if option == "user":
      legend = ["Id", "First name", "Last name", "Email", "Username", "Password", "Security key"]
    else:
      legend = ["User id", "Status"]

    data = EmployeeModels.workbench(option)
    return render_template("workbench.html", option = option, data = data, legend = legend)
  return render_template("workbench.html", option = None)