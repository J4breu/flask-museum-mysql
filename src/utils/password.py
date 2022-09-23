import string
import secrets

def generatePassword():
  alphabet = string.ascii_letters + string.digits
  password = ''.join(secrets.choice(alphabet) for i in range(6))
  return password