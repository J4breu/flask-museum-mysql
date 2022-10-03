from flask import Blueprint, flash, redirect, render_template, request
from flask_login import login_required, current_user

from ..utils.file import updateFile
from ..entities.client import Client
from ..models.clientModels import ClientModels

main = Blueprint("clientRoutes", __name__)

@main.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
  if (current_user.status != None):
      return redirect("/Profile")

  if request.method == "POST":
    image = updateFile(request.files["photography"])
    data = Client(
      None,
      request.form["bibliography"],
      request.form["birthDate"],
      request.form["nationality"],
      image
    )

    data = ClientModels.update(current_user.userId, data)
    return redirect("/home")

  data = ClientModels.edit(current_user.userId)
  return render_template("profile.html", data = data)