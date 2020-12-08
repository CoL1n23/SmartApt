import mysql.connector
import Credential
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

"""
CS348 Project

IMPORTANT: The conversion from unicode to ascii encoding should be noticed.
Each end will have to use different commands to convert information.
"""


def function2(room_num):
    engine = sqlalchemy.create_engine(
        'mysql+mysqlconnector://root:' + Credential.get_password() + '@34.68.129.232/smartapt',
        echo=True)

    Base = declarative_base()
    Base.metadata.create_all(engine)

    with engine.connect() as con:
        cursor = con.execute("SELECT R.RoomId, R.RoomType, R.Kitchen, R.NumOfBedrooms, R.NumOfBathrooms, R.Rent "
                             "FROM Room R "
                             "WHERE R.RoomId = \"" + room_num + "\";")

    room_info = ""
    counter = 0
    for line in cursor:
        for part in line:
            # IMPORTANT: Line below is for Colin's end
            if counter + 1 == len(line):
                room_info += str(part) + "\n"
            else:
                room_info += str(part) + ', '
                counter += 1

            # IMPORTANT: Line below is for Jeff's end
            # info += part.encode('ascii', 'ignore') + ',' + ' '

        counter = 0

    """
    # Establish connection to GCP SQL
    mydb = mysql.connector.connect(user=Credential.get_username(), password=Credential.get_password(),
                                   host='34.68.129.232',
                                   database='smartapt')

    cursor = mydb.cursor()

    # Define the query
    query = "SELECT R.RoomId, R.RoomType, R.Kitchen, R.NumOfBedrooms, R.NumOfBathrooms, R.Rent " \
            "FROM Room R " \
            "WHERE R.RoomId = \"" + room_num + "\";"

    cursor.execute(query)

    room_info = ""
    counter = 0
    for line in cursor:
        for part in line:
            # IMPORTANT: Line below is for Colin's end
            if counter + 1 == len(line):
                room_info += str(part) + "\n"
            else:
                room_info += str(part) + ', '
                counter += 1

            # IMPORTANT: Line below is for Jeff's end
            # info += part.encode('ascii', 'ignore') + ',' + ' '

        counter = 0

    cursor.close()
    mydb.close()
    """

    return room_info
