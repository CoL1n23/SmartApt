import mysql.connector
import Credential

"""
IMPORTANT: The conversion from unicode to ascii encoding should be noticed.
Each end will have to use different commands to convert information.
"""


def function1_1():
    # Establish connection to GCP SQL
    mydb = mysql.connector.connect(user=Credential.get_username(), password=Credential.get_password(),
                                   host='34.68.129.232',
                                   database='smartapt')

    cursor = mydb.cursor()

    # Define the query
    query = "SELECT R.Name, R.ResidentId, S.SchoolName, R.Career, R.RoomId, S.GraduationYear, S.Major " \
            "FROM Resident R JOIN Student S ON R.ResidentId = S.ResidentId " \
            "WHERE R.Career = \"Student\";"

    cursor.execute(query)

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

    cursor.close()
    mydb.close()

    return student_info


def function1_2():
    # Establish connection to GCP SQL
    mydb = mysql.connector.connect(user=Credential.get_username(), password=Credential.get_password(),
                                   host='34.68.129.232',
                                   database='smartapt')

    cursor = mydb.cursor()

    # Define the query
    query = "SELECT R.Name, R.ResidentId, E.CompanyName, R.Career, R.RoomId, E.Job, E.Salary, E.EducationStatus " \
            "FROM Resident R JOIN Employee E ON R.ResidentId = E.ResidentId " \
            "WHERE R.Career = \"Employee\";"

    cursor.execute(query)

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

    cursor.close()
    mydb.close()

    return employee_info
