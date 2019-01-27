# It is intented to serve to introduce CRUD differnt type of workloads to MySQL database to test failover behaviour
# All sample python scripts have error handling.  In case of any errors, it will sleep for 3 seconds and then re-connect to database.

python select.py 100
python insert.py 100
python delete.py 100

python total.py 100

where 100 is number of times to run

Required table:

create table test_users(user_name varchar(20), team varchar(20), created_dt DATETIME default current_timestamp);

