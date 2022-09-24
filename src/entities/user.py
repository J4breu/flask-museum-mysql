import string
import secrets
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
  def generatePassword(self):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(6))
    return password

  @classmethod
  def generateHash(self, password):
    return generate_password_hash(password)

  @classmethod
  def checkHash(self, hashed_password, password):
    return check_password_hash(hashed_password, password)