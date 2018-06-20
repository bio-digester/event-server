from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, Sensor, DataCollect, HOST, DATABASE, PASSWORD, USER

class Database(object):

    def __init__(self):
        self.host = 'postgres'
        self.user = 'raspberry_user'
        self.password = 'raspberry'
        self.database = 'raspberry_db'
        self.engine = None

    def _create_engine(self):
        self.engine = create_engine("postgresql+psycopg2://%s:%s@%s/%s" % 
            (self.user, self.password, self.host, self.database))

        DBSession = sessionmaker()
        DBSession.configure(bind = self.engine)
        session = DBSession()
        return session

    def _dispose(self):
        self.engine.dispose()
        
