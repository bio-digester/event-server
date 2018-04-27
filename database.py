import psycopg2
from datetime import datetime

HOST = 'postgres'
DATABASE = 'raspberry_db'
PASSWORD = 'raspberry'
USER = 'raspberry_user' 

def getSensorByName(name):
    con = psycopg2.connect(host = HOST, database = DATABASE,
                            user = USER, password = PASSWORD)
    cur = con.cursor()
    
    cur.execute("select * from sensors where name = '" + name + "'")
    recset = cur.fetchall()
    con.close()
    return recset

def setValue(sensorId, sensorValue):
    con = psycopg2.connect(host = HOST, database = DATABASE,
                            user = USER, password = PASSWORD)
    cur = con.cursor()
    
    cur.execute("insert into data_collects(data_measure, value," + 
                    " sensor_id, created_at, updated_at) " +
                    "VALUES (%s, %s, %s, %s, %s)",(datetime.now(), sensorValue,
                    sensorId, datetime.now(), datetime.now()))
    con.commit()
    con.close()

