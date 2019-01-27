#!/sur/bin/python
import mysql.connector,time
from mysql.connector import MySQLConnection,Error
from python_mysql_dbconfig import read_db_config

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print 'Number of times:', sys.argv[1]

def failover_test(t):

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
      my_cursor.execute("select count(*) from test_users")

      row = my_cursor.fetchone()

      while row is not None:
        print(row)
        row = my_cursor.fetchone()
    
      my_cursor.close()
      conn.close()

  except Error as e:
    print"Something went wrong:",e
    time.sleep(3)
    failover_test(counter)
    

  finally:
    print("============ Done ================")

failover_test(int(sys.argv[1]))
