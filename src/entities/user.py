from werkzeug.security import check_password_hash, generate_password_hash

class User():

  def __init__(self, id, firstName, lastName, email, username, password, securityKey) -> None:
    self.id = id
    self.firstName = firstName
    self.lastName = lastName
    self.email = email
    self.username = username
    self.password = password
    self.securityKey = securityKey

  @classmethod
  def generateHash(self, password):
    return generate_password_hash(password)

  @classmethod
  def checkHash(self, hashed_password, password):
    return check_password_hash(hashed_password, password)