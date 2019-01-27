#!/sur/bin/python
import mysql.connector,time
from mysql.connector import MySQLConnection,Error
from python_mysql_dbconfig import read_db_config
import sys
import time
from datetime import datetime

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print 'Number of times:', sys.argv[1]

def delete(t):

  try:
    new_counter = t

    if (t==int(sys.argv[1])):
	new_counter = 0

    for i in range(new_counter,int(sys.argv[1])):

      counter = i

      print("============ " + str(counter) + "/" + sys.argv[1] + "  ================")
    
      dbconfig = read_db_config()

      conn =  MySQLConnection(**dbconfig)

      if conn.is_connected():
        print('connection established.')
      else:
        print('connection failed.')

      my_cursor = conn.cursor()

      sql_delete_query = "DELETE FROM test_users LIMIT 1"

      result  = my_cursor.execute(sql_delete_query)
      conn.commit()

      print(my_cursor.rowcount, "record(s) deleted")

      my_cursor.close()
      conn.close()

  except Error as e:
    print"Something went wrong:",e
    time.sleep(3)
    delete(counter)
    

  finally:
    print("============ Done ================")

delete(int(sys.argv[1]))
