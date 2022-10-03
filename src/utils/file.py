import os
from .password import generatePassword
from werkzeug.utils import secure_filename

def updateFile(file):
  filename = secure_filename(file.filename)
  extension = os.path.splitext(filename)[1]
  name = generatePassword(20) + extension

  upload_path = os.path.join(("../flask-museum-mysql/src/static/img/upload"), name) 
  file.save(upload_path)

  return name