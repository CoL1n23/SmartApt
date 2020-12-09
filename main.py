from flask import Flask, render_template, request
import Function1
import Function2
import Function3
import Function4
import Function5
import Function6

"""
CS348 Project - SmartApt
Authors: Colin Wu, Jianwei Zhu
Date: 12/8/20

ORM (SQLAlchemy) is implemented in order to develop a secure query execution.

IMPORTANT: The conversion from unicode to ascii encoding should be noticed.
Each author will have to use different commands to convert information on their ends.
"""


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/func1')
def function1_page():
    f1Content_1 = Function1.function1_1()
    f1Content_2 = Function1.function1_2()
    return render_template("function_1.html", data1=f1Content_1, data2=f1Content_2)


@app.route('/func2')
def function2():
    return render_template("room.html")


@app.route('/func2', methods=['POST'])
def function2_page():
    text = request.form['text']
    processed_text = text.upper()

    f2Content = Function2.function2(processed_text)
    return render_template("function_2.html", data=f2Content)


@app.route('/func3')
def function3():
    return render_template("applicant.html")


@app.route('/func3', methods=['POST'])
def function3_page():
    name = request.form['name']
    career = request.form['career']
    residentId = request.form['residentId']
    plateNum = request.form['plateNum']
    roomId = request.form['roomId']

    Function3.function3(name, career, residentId, plateNum, roomId)

    return render_template("function_3.html")


@app.route('/func4')
def function4():
    return render_template("student.html")


@app.route('/func4', methods=['POST'])
def function4_page():
    name = request.form['name']
    schoolName = request.form['schoolName']
    studentId = request.form['studentId']
    graduationYear = request.form['graduationYear']
    residentId = request.form['residentId']
    major = request.form['major']

    Function4.function4(name, schoolName, studentId, graduationYear, residentId, major)

    return render_template("function_4.html")


@app.route('/func5')
def function5():
    return render_template("employee.html")


@app.route('/func5', methods=['POST'])
def function5_page():
    name = request.form['name']
    companyName = request.form['companyName']
    job = request.form['job']
    salary = request.form['salary']
    residentId = request.form['residentId']
    educationStatus = request.form['educationStatus']

    Function5.function5(name, companyName, job, salary, residentId, educationStatus)

    return render_template("function_5.html")


@app.route('/func6')
def function6():
    return render_template("delete.html")


@app.route('/func6', methods=['POST'])
def function6_page():
    residentId = request.form['residentId']
    Function6.function6(residentId)
    return render_template("function_6.html")


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1", debug=True)