from ..utils.db import getConnection
from ..entities.user import User

class UserModels():
  @classmethod
  def login(self, user):
    sql = """
          SELECT  id,
                  firstName,
                  lastName,
                  email, 
                  username, 
                  password,
                  securityKey
          FROM user WHERE email = '{}'
        """.format(user.email)
    try:
      connection = getConnection()

      with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchone()
        if (row != None):
          user = User(row[0],
                      row[1],
                      row[2],
                      row[3],
                      row[4],
                      User.checkHash(row[5], user.password),
                      row[6])
          return user
        return None
    
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def forgotPassword(self, user):
    sql = "SELECT securityKey FROM user WHERE email = '{}'".format(user.email)
    try:
      connection = getConnection()

      with connection.cursor() as cursor:
        cursor.execute(sql)
        field = cursor.fetchone()

        sql = "UPDATE user SET password = '{}' WHERE email = '{}'".format(User.generateHash(user.password), user.email)

        if (field != None and User.checkHash(field[0], user.securityKey)):
          cursor.execute(sql)
          connection.commit()
          connection.close()
          return user
        return None
    
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def registration(self, user):
    sql = """
          INSERT INTO user (firstName, 
                            lastName, 
                            email, 
                            username, 
                            password,
                            securityKey)
          VALUES (%s, %s, %s, %s, %s, %s)
        """
    values = (user.firstName, 
              user.lastName, 
              user.email, 
              user.username, 
              User.generateHash(user.password),
              User.generateHash(user.securityKey))
    try:
      connection = getConnection()

      with connection.cursor() as cursor:
        cursor.execute(sql, values)
        connection.commit()
      connection.close()
      return None

    except Exception as ex:
      raise Exception(ex)