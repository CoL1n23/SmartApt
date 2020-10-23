import mysql.connector

# Establish connection to GCP SQL
mydb = mysql.connector.connect(user='root', password='CS348',
                               host='34.68.129.232',
                               database='smartapt')

cursor = mydb.cursor()

query = "SELECT R.Name, R.ResidentId, S.SchoolName FROM Resident R JOIN Student S ON R.ResidentId = S.ResidentId;"

cursor.execute(query)

for line in cursor:
    print(line)

cursor.close()
mydb.close()
