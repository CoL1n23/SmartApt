from flask import Flask, render_template
import Function1

app = Flask(__name__)


@app.route('/')
def index():
    msg = "CS348 Project, Purdue University"
    return render_template("index.html", data=msg)


@app.route('/func1')
def function1_page():
    f1Content_1 = Function1.function1_1()
    f1Content_2 = Function1.function1_2()
    return render_template("function_1.html", data1=f1Content_1, data2=f1Content_2)


@app.route('/func2')
def function2_page():
    f2Content = "room_info"
    return render_template("function_2.html", data=f2Content)


@app.route('/func3')
def function3_page():
    f3Content = "registration"
    return render_template("function_3.html", data=f3Content)


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1", debug=True)