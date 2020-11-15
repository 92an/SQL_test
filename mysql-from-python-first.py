import os
import datetime
import pymysql

# Get username
username = os.getenv("C9_USER")


# Conncect to Database
connection = pymysql.connect(
                            host="localhost",
                            user=username,
                            password="",
                            db="Chinook")

# Insert example:
""" try:
    with connection.cursor() as cursor:
        row = [("Bob", 21, "1990-02-10 23:10:10"), 
                ("Fred", 61, "1960-02-10 20:10:10"),
                ("Jim", 101, "1920-02-10 15:10:10")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
finally:
    # Close connection.
    connection.close() """


try:
    with connection.cursor() as cursor:
        list_of_names = ['Fred', 'Bob']
        format_strings = ",".join(["%s"]*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names )
        connection.commit()
finally:
    # Close connection.
    connection.close()