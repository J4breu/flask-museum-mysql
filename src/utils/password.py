import string
import secrets

def generatePassword(num):
  alphabet = string.ascii_letters + string.digits
  password = ''.join(secrets.choice(alphabet) for i in range(num))
  return password