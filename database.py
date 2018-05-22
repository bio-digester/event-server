import psycopg2
from datetime import datetime

class Database(object):
    HOST = 'postgres'
    DATABASE = 'raspberry_db'
    PASSWORD = 'raspberry'
    USER = 'raspberry_user' 

    def connect(self):
        return psycopg2.connect(host = self.HOST, database = self.DATABASE,
                user = self.USER, password = self.PASSWORD)

    def getSensorByName(self, name):
        con = self.connect()
        cur = con.cursor()
        cur.execute("select * from sensors where name = '" + name + "'")
        recset = cur.fetchall()
        con.close()
        return recset

    def setValue(self, sensorId, sensorValue):
        con = self.connect()
        cur = con.cursor()
        cur.execute("insert into data_collects(data_measure, value," + 
                " sensor_id) " +
                "VALUES (%s, %s, %s)",(datetime.now(), sensorValue,
                    sensorId))
        con.commit()
        con.close()

