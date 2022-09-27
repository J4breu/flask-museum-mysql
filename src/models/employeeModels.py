from ..utils.db import getConnection
from ..entities.user import User

class EmployeeModels():
  @classmethod
  def workbench(self, option):
    try:
      connection = getConnection()

      if option == "user":
        sql = "SELECT * FROM user"
      if option == "employee":
        sql = "SELECT * FROM employee"
      if option == "art":
        sql = "SELECT * FROM art"

      with connection.cursor() as cursor:
        cursor.execute(sql)
        return cursor.fetchall()

    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def create(self, option, legend):
    if option == "user":
      sql = """
            INSERT INTO user (firstName, 
                              lastName, 
                              email, 
                              username, 
                              password,
                              securityKey)
            VALUES (%s, %s, %s, %s, %s, %s)
          """
      values = (legend.firstName, 
                legend.lastName, 
                legend.email, 
                legend.username, 
                User.generateHash(legend.password),
                User.generateHash(legend.securityKey))

    if option == "employee":
      sql = """
            INSERT INTO employee (userId, 
                            status)
            VALUES (%s, %s)
          """
      values = (legend.userId,
                legend.status)
    try:
      connection = getConnection()

      with connection.cursor() as cursor:
        cursor.execute(sql, values)
        connection.commit()
      connection.close()
      return None

    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def edit(self, option, legend, id):
    if option == "user":
      sql = """
            UPDATE user
            SET id = %s,
                firstName = %s, 
                lastName = %s, 
                email = %s, 
                username = %s, 
                password = %s,
                securityKey = %s
            WHERE id = %s
          """
      values = (legend.id,
                legend.firstName, 
                legend.lastName, 
                legend.email, 
                legend.username, 
                User.generateHash(legend.password),
                User.generateHash(legend.securityKey),
                id)

    if option == "employee":
      sql = """
            UPDATE user
            SET userId = %s,
                status = %s
            WHERE id = %s
          """
      values = (legend.userId,
                legend.status,
                id)
    try:
      connection = getConnection()

      with connection.cursor() as cursor:
        cursor.execute(sql, values)
        connection.commit()
      connection.close()
      return None

    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def delete(self, option, id):
    try:
      connection = getConnection()
      with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM {option} WHERE id = {id}")
        connection.commit()
      connection.close()
      return None

    except Exception as ex:
      raise Exception(ex)
