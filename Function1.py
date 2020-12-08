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


def function1_1():
    engine = sqlalchemy.create_engine(
        'mysql+mysqlconnector://root:' + Credential.get_password() + '@34.68.129.232/smartapt',
        echo=True, isolation_level='READ_COMMITTED')

    Base = declarative_base()
    Base.metadata.create_all(engine)

    with engine.connect() as con:
        cursor = con.execute("SELECT R.Name, R.ResidentId, S.SchoolName, R.Career, R.RoomId, S.GraduationYear, S.Major "
                             "FROM Resident R JOIN Student S ON R.ResidentId = S.ResidentId "
                             "WHERE R.Career = \"Student\";")

    """
    table = "<html> <table border = '1'>"

    for (name, residentId, schoolName, career, roomId, graduateYear, major) in cursor:
        table = table + "<tr>\n"
        table = table + "<td>" + name + "</td>"
        table = table + "<td>" + residentId + "</td>"
        table = table + "<td>" + schoolName + "</td>"
        table = table + "<td>" + career + "</td>"
        table = table + "<td>" + roomId + "</td>"
        table = table + "<td>" + str(graduateYear) + "</td>"
        table = table + "<td>" + major + "</td>"
        table = table + "</tr>\n"

    table = table + "</table> </html>"

    return table

    """

    student_info = ""
    counter = 0
    for line in cursor:
        for part in line:
            # IMPORTANT: Line below is for Colin's end
            if counter + 1 == len(line):
                student_info += str(part) + "\n"
            else:
                student_info += str(part) + ', '
                counter += 1

            # IMPORTANT: Line below is for Jeff's end
            # info += part.encode('ascii', 'ignore') + ',' + ' '

        counter = 0

    return student_info


def function1_2():
    engine = sqlalchemy.create_engine(
        'mysql+mysqlconnector://root:' + Credential.get_password() + '@34.68.129.232/smartapt',
        echo=True, isolation_level='READ_COMMITTED')

    Base = declarative_base()
    Base.metadata.create_all(engine)

    with engine.connect() as con:
        cursor = con.execute(
            "SELECT R.Name, R.ResidentId, E.CompanyName, R.Career, R.RoomId, E.Job, E.Salary, E.EducationStatus "
            "FROM Resident R JOIN Employee E ON R.ResidentId = E.ResidentId "
            "WHERE R.Career = \"Employee\";")

    employee_info = ""
    counter = 0
    for line in cursor:
        for part in line:
            # IMPORTANT: Line below is for Colin's end
            if counter + 1 == len(line):
                employee_info += str(part) + "\n"
            else:
                employee_info += str(part) + ', '
                counter += 1

            # IMPORTANT: Line below is for Jeff's end
            # info += part.encode('ascii', 'ignore') + ',' + ' '

        counter = 0

    return employee_info
