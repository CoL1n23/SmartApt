import mysql.connector
import Credential

"""
IMPORTANT: The conversion from unicode to ascii encoding should be noticed.
Each end will have to use different commands to convert information.
"""


def function1():
    # Establish connection to GCP SQL
    mydb = mysql.connector.connect(user=Credential.get_username(), password=Credential.get_password(),
                                   host='34.68.129.232',
                                   database='smartapt')

    cursor = mydb.cursor()

    # Define the query
    query = "SELECT R.Name, R.ResidentId, S.SchoolName, R.Career, R.RoomId, S.GraduationYear, S.Major" \
            " FROM Resident R JOIN Student S ON R.ResidentId = S.ResidentId;"

    cursor.execute(query)

    info = ""
    counter = 0
    for line in cursor:
        for part in line:
            # IMPORTANT: Line below is for Colin's end
            if counter + 1 == len(line):
                info += str(part) + "\n"
            else:
                info += str(part) + ', '
                counter += 1

            # IMPORTANT: Line below is for Jeff's end
            # info += part.encode('ascii', 'ignore') + ',' + ' '

        counter = 0

    cursor.close()
    mydb.close()

    return info
