
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = "secret"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'student_db'

mysql = MySQL(app)

@app.route('/')
def dashboard():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT COUNT(*) AS total FROM students")
    student_count = cursor.fetchone()['total']
    cursor.execute("SELECT COUNT(*) AS total FROM attendance")
    attendance_count = cursor.fetchone()['total']
    cursor.execute("SELECT COUNT(*) AS total FROM records")
    record_count = cursor.fetchone()['total']
    return render_template('dashboard.html',
                           student_count=student_count,
                           attendance_count=attendance_count,
                           record_count=record_count)

@app.route('/students')
def students():
    c = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    c.execute("SELECT * FROM students")
    return render_template('students.html', students=c.fetchall())

@app.route('/students/add', methods=['POST','GET'])
def add_student():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        dept=request.form['dept']
        c=mysql.connection.cursor()
        c.execute("INSERT INTO students(name,email,department) VALUES(%s,%s,%s)",(name,email,dept))
        mysql.connection.commit()
        flash("Student added","success")
        return redirect(url_for('students'))
    return render_template('add_student.html')

@app.route('/attendance')
def attendance():
    c = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    c.execute("SELECT * FROM attendance")
    return render_template('attendance.html', data=c.fetchall())

@app.route('/attendance/add', methods=['POST','GET'])
def add_attendance():
    if request.method=='POST':
        sid=request.form['sid']
        status=request.form['status']
        c=mysql.connection.cursor()
        c.execute("INSERT INTO attendance(student_id,status) VALUES(%s,%s)",(sid,status))
        mysql.connection.commit()
        flash("Attendance added","info")
        return redirect(url_for('attendance'))
    return render_template('add_attendance.html')

@app.route('/records')
def records():
    c = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    c.execute("SELECT * FROM records")
    return render_template('records.html', data=c.fetchall())

@app.route('/records/add', methods=['POST','GET'])
def add_record():
    if request.method=='POST':
        sid=request.form['sid']
        subject=request.form['subject']
        marks=request.form['marks']
        c=mysql.connection.cursor()
        c.execute("INSERT INTO records(student_id,subject,marks) VALUES(%s,%s,%s)",(sid,subject,marks))
        mysql.connection.commit()
        flash("Record added","info")
        return redirect(url_for('records'))
    return render_template('add_record.html')

if __name__=='__main__':
    app.run(debug=True)
