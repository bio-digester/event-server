from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
HOST = 'postgres'
DATABASE = 'raspberry_db'
PASSWORD = 'raspberry'
USER = 'raspberry_user'

class Sensor(Base):

    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    codename = Column(String(250))

    def __repr__(self):
        return "<Sensor(id='%s', name='%s', codename='%s)>" % (
                                self.id, self.name, self.codename) 

class DataCollect(Base):

    __tablename__ = 'data_collects'

    id = Column(Integer, primary_key=True)
    data_measure = Column(DateTime)
    value = Column(String(250))
    sensor_id = Column(Integer, ForeignKey('sensors.id'))
    sensor = relationship(Sensor)
 
    def __repr__(self):
        return "<DataCollect(id='%s', data_measure='%s', value='%s', sensor=%s)>" % (
                                self.id, self.data_measure, self.value, self.sensor)

class Notification(Base):
    __tablename__ = 'notification'

    id = Column(Integer, primary_key=True)
    message_date = Column(DateTime)
    message = Column(String(250))
    
    def __repr__(self):
        return "<Report(id='%s', date='%s', message='%s')>" % (
                                self.id, self.message_date, self.message)


engine = create_engine("postgresql+psycopg2://raspberry_user:raspberry@postgres/raspberry_db") 
Base.metadata.create_all(engine)


