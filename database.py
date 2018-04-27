import psycopg2
from datetime import datetime

def getSensorByName(name):
    con = psycopg2.connect(host='postgres', database='raspberry_db',
    user='raspberry_user', password='raspberry')
    cur = con.cursor()
    
    cur.execute("select * from sensors where name = '" + name + "'")
    recset = cur.fetchall()
    con.close()
    return recset

#def setValue(sensorId, sensorValue):
#    con = psycopg2.connect(host='postgres', database='raspberry_db',
#    user='raspberry_user', password='raspberry')
#    cur = con.cursor()
#    
#    cur.execute("insert into data_collects(data_measure, value, sensor_id) " +
#                    "VALUES ('" + datetime.now() + "'," + sensorValue + "," + sensorId + ")")
#    con.close()
#
