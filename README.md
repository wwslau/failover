# failover

python select.py 100
python insert.py 100
python delete.py 100

python total.py 100

where 100 is number of times to run

Required table:

create table test_users(user_name varchar(20), team varchar(20), created_dt DATETIME default current_timestamp);

