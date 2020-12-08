import mysql.connector
import Credential
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

"""
CS348 Project

IMPORTANT: The conversion from unicode to ascii encoding should be noticed.
Each end will have to use different commands to convert information.

ORM is implemented in order to develop a secure query execution.
"""


def function5(name, companyName, job, salary, residentId, educationStatus):
    engine = sqlalchemy.create_engine(
        'mysql+mysqlconnector://root:' + Credential.get_password() + '@34.68.129.232/smartapt',
        echo=True)

    Base = declarative_base()

    class Employee(Base):
        __tablename__ = 'Employee'

        name = sqlalchemy.Column(sqlalchemy.String(length=50))
        companyName = sqlalchemy.Column(sqlalchemy.String(length=50))
        job = sqlalchemy.Column(sqlalchemy.String(length=50))
        salary = sqlalchemy.Column(sqlalchemy.Integer)
        residentId = sqlalchemy.Column(sqlalchemy.String(length=50), primary_key=True)
        educationStatus = sqlalchemy.Column(sqlalchemy.String(length=50))

        def __repr__(self):
            return "<Employee(name='{1}', companyName='{1}', job='{1}', salary='{1}', residentId='{0}', " \
                   "educationStatus='{1}')>".format(
                self.name, self.companyName, self.job, self.salary, self.residentId, self.educationStatus)

    Base.metadata.create_all(engine)

    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    newEmployee = Employee(name=name, companyName=companyName, job=job, salary=salary, residentId=residentId,
                           educationStatus=educationStatus)
    session.add(newEmployee)

    session.commit()
