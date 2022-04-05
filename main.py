from flask import Flask, render_template,request,redirect
import sqlite3
conn=sqlite3.connect("studentmanagement.db", check_same_thread=False)

listOfTables=conn.execute("SELECT name from sqlite_master WHERE type='table' AND name='STUDENT' ").fetchall()

if listOfTables!=[]:
    print("Table Already Exists ! ")
else:
    conn.execute(''' CREATE TABLE STUDENT(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT, COLLEGE_NAME TEXT, BRANCH TEXT, 
    ADMNO INTEGER DOB TEXT,PASSWORD TEXT
    ); ''')
    print("Table has created")



app = Flask(__name__)

@app.route("/")
def StudentData():
    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def registerStudent():
    if request.method=="POST":
        getName=request.form["name"]
        getClgName=request.form["college_name"]
        getBranch=request.form["branch"]
        getAdmno=request.form["admno"]
        getdob=request.form["dob"]
        getpass=request.form["pass"]
        getCnfPass=request.form["cnf_pass"]

        print(getName)
        print(getClgName)
        print(getBranch)
        print(getAdmno)
        print(getdob)
        print(getpass)
        print(getCnfPass)
        try:
            conn.execute("INSERT INTO STUDENT (name,COLLEGE_NAME,BRANCH,ADMNO,PASSWORD,DOB) VALUES ('"+getName+"','"+getClgName+"','"+getBranch+"','"+getAdmno+"','"+getpass+"','"+getdob+"')")
            print("Successfully inserted")
            return redirect()
        except Exception as e:
            print(e)
    return render_template("register.html")

@app.route("/viewall")
def view():
    cursor=conn.cursor()
    cursor.execute("SELECT *FROM STUDENT")
    result=cursor.fetchall()
    return render_template("viewall.html",students=result)

@app.route("/search")
def searchStudent():
    return render_template("search.html")

@app.route("/delete")
def deleteStudent():
    return render_template("delete.html")

if __name__=="__main__":
    app.run()