from ..utils.db import getConnection
from ..entities.user import User
from ..entities.employee import Employee

class EmployeeModels():
  @classmethod
  def create(self, option, data):
    if option == "user":
      sql = """
        INSERT INTO user (firstName, lastName, email, username, password, securityKey)
        VALUES ('{}', '{}', '{}', '{}', '{}', '{}')
      """.format(
        data.firstName, 
        data.lastName, 
        data.email, 
        data.username, 
        User.generateHash(data.password),
        User.generateHash(data.securityKey)
      )

    if option == "employee":
      sql = """
        INSERT INTO employee (userId, status)
        VALUES ({}, '{}')
      """.format(data.userId, data.status)
    try:
      connection = getConnection()

      with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
      connection.close()
      return None

    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def delete(self, option, id):
    if option == "user":
      sql = f"DELETE FROM {option} WHERE id = {id}"
    if option == "employee":
      sql = f"DELETE FROM {option} WHERE userId = {id}"
    try:
      connection = getConnection()
      with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
      connection.close()
      return None

    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def edit(self, option, id):
    if option == "user":
      sql = f"SELECT * FROM {option} WHERE id = {id}"
    if option == "employee":
      sql = f"SELECT * FROM {option} WHERE userId = {id}"
    try:
      connection = getConnection()
      with connection.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchall()
      return data[0]

    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def getById(self, userId):
    sql = f"SELECT * FROM employee WHERE userId = '{userId}'"
    try:
      connection = getConnection()

      with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchone()
        
        data = Employee(userId, None)
        
        if (row != None):
          data = Employee(row[0], row[1])
        return data
    
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def update(self, option, data, id):
    if option == "user":
      sql = """
        UPDATE user
        SET id = {}, firstName = '{}', lastName = '{}', email = '{}', username = '{}', password = '{}', securityKey = '{}'
        WHERE id = {}
      """.format(
        data.id,
        data.firstName, 
        data.lastName, 
        data.email, 
        data.username, 
        User.generateHash(data.password),
        User.generateHash(data.securityKey),
        id
      )

    if option == "employee":
      sql = """
        UPDATE employee
        SET userId = {}, status = '{}'
        WHERE userId = {}
      """.format(data.userId, data.status, id)
    try:
      connection = getConnection()

      with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
      connection.close()
      return None

    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def workbench(self, option):
    try:
      connection = getConnection()

      if option == "user":
        sql = "SELECT * FROM user"
      if option == "employee":
        sql = "SELECT * FROM employee"

      with connection.cursor() as cursor:
        cursor.execute(sql)
        return cursor.fetchall()

    except Exception as ex:
      raise Exception(ex)