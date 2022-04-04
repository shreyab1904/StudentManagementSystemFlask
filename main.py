from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def StudentData():
    return "<h1>Student data<h1>"

@app.route("/register")
def registerStudent():
    return render_template("register.html")

@app.route("/search")
def searchStudent():
    return render_template("search.html")

@app.route("/delete")
def deleteStudent():
    return render_template("delete.html")

if __name__=="__main__":
    app.run()