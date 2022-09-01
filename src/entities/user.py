from werkzeug.security import check_password_hash, generate_password_hash

class User():

  def __init__(self, id, firstName, lastName, email, username, password) -> None:
    self.id = id
    self.firstName = firstName
    self.lastName = lastName
    self.email = email
    self.username = username
    self.password = password

  @classmethod
  def generatePassword(self, password):
    return generate_password_hash(password)

  @classmethod
  def checkPassword(self, hashed_password, password):
    return check_password_hash(hashed_password, password)