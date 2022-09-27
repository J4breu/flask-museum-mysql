from flask import Blueprint, redirect,render_template, request

main = Blueprint("userArt", __name__)

from ..entities.art import Art
from ..models.artModels import ArtModels

@main.route('/addArt', methods=['GET', 'POST'])
def addart():
  if request.method == "POST":
    title = request.form["title"]
    imageLink = request.form["imageLink"]
    gender = request.form["gender"]
    status = "a"
    author = "a"
    price = "a"
    commision = "a"

    art = Art(0,
              title,
              imageLink,
              gender,
              status,
              author,
              price,
              commision)

    ArtModels.add(art)
    return redirect("home/client")
  return render_template('addArt.html')
