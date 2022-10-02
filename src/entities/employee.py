from flask_login import UserMixin

class Employee(UserMixin):

  def __init__(self, userId, status) -> None:
    self.userId = userId
    self.status = status