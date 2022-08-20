import mysql.connector
from mysql.connector import Error
from clickhouse_driver import Client
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def databaseactivity(self):

 connection = mysql.connector.connect(host='164.52.223.139',
                                         database='terrier_1',
                                         user='admin',
                                         password='carinov@123')
 print("We are cone")
 mycursor = connection.cursor()
 print("We are cone")
 mycursor.execute("select status ,count(status)from(select server_name ,server_status as status from recording_server rs where is_disabled = 0) as a group by status")
 myresult = mycursor.fetchall()
 print(myresult)
 expecte=myresult
 print("We are cone")
 return expecte


def clickhouse(self):
 conn_str = 'clickhouse://default:@localhost/default'
 engine = create_engine(conn_str)
 session = sessionmaker(bind=engine)()