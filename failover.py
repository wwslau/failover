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

      print 'Counter:', counter
    
      dbconfig = read_db_config()

      conn =  MySQLConnection(**dbconfig)

      if conn.is_connected():
        print('connection established.')
      else:
        print('connection failed.')

      cursor = conn.cursor()
      cursor.execute("select host,user from user")

      row = cursor.fetchone()

      while row is not None:
        print(row)
        row = cursor.fetchone()
    
      cursor.close()
      conn.close()

  except Error as e:
    print("something went wrong!")
    print(e)
    print 'Current counter:',counter
    time.sleep(3)
    failover_test(counter)
    

  finally:
    print("============ Done ================")

failover_test(int(sys.argv[1]))
