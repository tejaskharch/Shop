from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="goal@25",
    database="shop"
)

cursor = db.cursor()
@app.route('/<parkCode>', methods=['POST'])
def index(parkCode):
    if request.method == 'POST':
        fname = request.form['firstname']
        lname = request.form['lastname']
        email = request.form['email']
        phone_no = request.form['phone_number']
        gender = request.form['gender']
        password = request.form['confirm_password']
        
        insert_query = "INSERT INTO user(fname,lname,email,ph_no,gender,password) VALUES (%s,%s,%s,%s,%s,%s)"
        data = (fname,lname,email,phone_no,gender,password)

        cursor.execute(insert_query, data)
        db.commit()
        return redirect(url_for('success'))
    return render_template('signup.html',parkCode=parkCode)
   

