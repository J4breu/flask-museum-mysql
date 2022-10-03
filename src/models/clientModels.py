from ..utils.db import getConnection

from ..entities.client import Client

class ClientModels():
  @classmethod
  def new(self, email):
    sql = f"SELECT * FROM user WHERE email = '{email}'"

    image = "example.png"
    try:
      connection = getConnection()

      with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchone()

        if (row != None):
          sql = """
            INSERT INTO client (userId, bibliography, birthDate, nationality, photography)
            VALUES ('{}', '{}', '{}', '{}', '{}')
          """.format(row[0], None, None, None, image)
          cursor.execute(sql)
          connection.commit()
          connection.close()
        return None

    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def edit(self, userId):
    sql = f"SELECT * FROM client WHERE userId = {userId}"
    try:
      connection = getConnection()
      with connection.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchall()
      return data[0]

    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def update(self, userId, data):
    sql = """
      UPDATE client
      SET bibliography = '{}', birthDate = '{}', nationality = '{}', photography = '{}'
      WHERE userId = {}
    """.format(data.bibliography, data.birthDate, data.nationality, data.photography, userId)
    try:
      connection = getConnection()

      with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
      connection.close()
      return None

    except Exception as ex:
      raise Exception(ex)