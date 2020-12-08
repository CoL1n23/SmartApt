import mysql.connector
import Credential
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

"""
CS348 Project - SmartApt
Authors: Colin Wu, Jianwei Zhu
Date: 12/8/20

ORM (SQLAlchemy) is implemented in order to develop a secure query execution.

IMPORTANT: The conversion from unicode to ascii encoding should be noticed.
Each author will have to use different commands to convert information on their ends.
"""


def function3(name, career, residentId, plateNum, roomId):
    engine = sqlalchemy.create_engine(
        'mysql+mysqlconnector://root:' + Credential.get_password() + '@34.68.129.232/smartapt',
        echo=True, isolation_level='REPEATABLE_READ')

    Base = declarative_base()

    class Resident(Base):
        __tablename__ = 'Resident'

        name = sqlalchemy.Column(sqlalchemy.String(length=50))
        career = sqlalchemy.Column(sqlalchemy.String(length=50))
        residentId = sqlalchemy.Column(sqlalchemy.String(length=50), primary_key=True)
        plateNum = sqlalchemy.Column(sqlalchemy.String(length=50))
        roomId = sqlalchemy.Column(sqlalchemy.String(length=50))

        def __repr__(self):
            return "<Resident(name='{1}', career='{1}', residentId='{0}', plateNum='{1}', roomId='{1}')>".format(
                self.name, self.career, self.residentId, self.plateNum, self.roomId)

    Base.metadata.create_all(engine)

    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    newResident = Resident(name=name, career=career, residentId=residentId, plateNum=plateNum, roomId=roomId)
    session.add(newResident)

    session.commit()
