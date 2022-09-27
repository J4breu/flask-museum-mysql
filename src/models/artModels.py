from ..utils.db import getConnection
from ..entities.art import *

class ArtModels():
  @classmethod
  def add(self, art):
    sql = """
          INSERT INTO art (title,
                          imageLink, 
                          gender,
                          author, 
                          price)
          VALUES (%s, %s, %s, %s, %s)
        """
    values = (art.title,
							art.imageLink,
              art.gender,
              art.author, 
              art.price
							)
    try:
      connection = getConnection()

      with connection.cursor() as cursor:
        cursor.execute(sql, values)
        connection.commit()
        connection.close()
      return None

    except Exception as ex:
      raise Exception(ex)