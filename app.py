from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# ----------------------------
# MONGODB CONNECTION
# ----------------------------
client = MongoClient("mongodb+srv://02fe23bcs192_db_user:nkrTxp4yv0TWq107@cluster0.u1pzuoc.mongodb.net/?appName=Cluster0")

db = client["attendanceDB"]       # database name
collection = db["records"]        # collection name


# ----------------------------
# ROUTE - FORM PAGE
# ----------------------------
@app.route('/')
def home():
    return render_template('form.html')


# ----------------------------
# ROUTE - HANDLE FORM SUBMISSION
# ----------------------------
@app.route('/submit', methods=['POST'])
def submit():
    emp_id = request.form['employeeID']
    date = request.form['date']
    attendance = request.form['attendance']

    record = {
        "EmployeeID": emp_id,
        "Date": date,
        "Attendance": attendance
    }

    collection.insert_one(record)

    return f"Attendance saved successfully for Employee {emp_id}!"


# ----------------------------
# RUN FLASK
# ----------------------------
if __name__ == "__main__":
    app.run()
