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

    def getBestValues(self):
        # we can't have best table implemented
        pass

    def __getLastSensorValue(self, name):
        sensor_id = self.getSensorByName(name)

        con = self.connect()
        cur = con.cursor()
        cur.execute("select value from data_collects where sensor_id = " +
            str(sensor_id[0][0]) + " order by data_measure DESC limit 1")
        recset = cur.fetchone()
        con.close()
        return recset[0]

    def getLastSensorsValues(self):
        sensors = {}
        sensors['TEMPDS'] = float(self.__getLastSensorValue('TEMPDS')) 
        print(sensors)
        return sensors





