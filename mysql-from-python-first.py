import os
import pymysql

# Get username
username = os.getenv("C9_USER")


# Conncect to Database
connection = pymysql.connect(
                            host="localhost",
                            user=username,
                            password="",
                            db="Chinook")
try:
    # Run a Query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    # Close connection.
    connection.close()