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


def function4(name, schoolName, studentId, graduationYear, residentId, major):
    engine = sqlalchemy.create_engine(
        'mysql+mysqlconnector://root:' + Credential.get_password() + '@34.68.129.232/smartapt',
        echo=True, isolation_level='REPEATABLE_READ')

    Base = declarative_base()

    class Student(Base):
        __tablename__ = 'Student'

        name = sqlalchemy.Column(sqlalchemy.String(length=50))
        schoolName = sqlalchemy.Column(sqlalchemy.String(length=50))
        studentId = sqlalchemy.Column(sqlalchemy.String(length=50))
        graduationYear = sqlalchemy.Column(sqlalchemy.Integer)
        residentId = sqlalchemy.Column(sqlalchemy.String(length=50), primary_key=True)
        major = sqlalchemy.Column(sqlalchemy.String(length=50))

        def __repr__(self):
            return "<Student(name='{1}', schoolName='{1}', studentId='{1}', graduationYear='{1}', residentId='{0}')" \
                   "major='{1}'>".format(
                self.name, self.schoolName, self.studentId, self.graduationYear, self.residentId, self.major)

    Base.metadata.create_all(engine)

    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    newStudent = Student(name=name, schoolName=schoolName, studentId=studentId, graduationYear=graduationYear,
                         residentId=residentId, major=major)
    session.add(newStudent)

    session.commit()
