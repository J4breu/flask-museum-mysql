from decouple import config
from mysql import connector

def getConnection():
  try:
    return connector.connect(
      host = config('MYSQL_HOST'),
      port = config('MYSQL_PORT'),
      user = config('MYSQL_USER'),
      password = config('MYSQL_PASSWORD'),
      db = config('MYSQL_DB')
    )

  except Exception as ex:
    raise Exception(ex)