from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


@app.route('/')
def index():
    msg = "CS 348 Project, Purdue University"
    return render_template("index.html", data=msg)


@app.route('/func1')
def function1_page():
    f1Content = function1()
    return render_template("function_1.html", data=f1Content)


@app.route('/func2')
def function2_page():
    f2Content = "room_info"
    return render_template("function_2.html",data=f2Content)


@app.route('/func3')
def function3_page():
    f3Content = "registration"
    return render_template("function_3.html",data=f3Content)


def function1():
    # Establish connection to GCP SQL
    mydb = mysql.connector.connect(user='root', password='CS348',
                                   host='34.68.129.232',
                                   database='smartapt')

    cursor = mydb.cursor()

    # Define the query
    query = 'SELECT R.Name, R.ResidentId, S.SchoolName FROM Resident R JOIN Student S ON R.ResidentId = S.ResidentId;'

    cursor.execute(query)

    info = ""
    for line in cursor:
        for part in line:
            info += part.encode('ascii', 'ignore') + ',' + ' '

    cursor.close()
    mydb.close()
    return str


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1", debug=True)