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

def insert(t):

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

      my_cursor = conn.cursor(prepared=True)

      sql_insert_date_query = """ INSERT INTO `test_users`
                              (`user_name`, `team`, `created_dt`) VALUES (%s,%s,%s)"""

      current_Date = datetime.now()
      formatted_date = current_Date.strftime('%Y-%m-%d %H:%M:%S')

      insert_tuple = ('Member1', 'team', current_Date)
      print 'Insert_tuple:', insert_tuple
      
      result  = my_cursor.execute(sql_insert_date_query,insert_tuple)
      conn.commit()

      my_cursor.close()
      conn.close()

  except Error as e:
    print"Something went wrong:",e
    time.sleep(3)
    insert(counter)
    

  finally:
    print("============ Done ================")

insert(int(sys.argv[1]))
