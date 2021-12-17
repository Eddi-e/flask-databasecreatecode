from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
import sqlite3
import random
from hashfunction import hashfunc

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return redirect(url_for('login'))


@app.route("/signup", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        email=request.form["email"]
        password=hashfunc(request.form["password"])
        con = sqlite3.connect('databaseforwebapp.db')
        cursor = con.cursor()
        #try:
#          for row in cursor.execute("SELECT userID FROM user WHERE email=trim(?)",(email,)):#trim function removes extra spaces
#              list.append("")
        cursor.execute(
            "INSERT INTO user (email, password) VALUES (?, ?)",
            (email, password),
            )
        con.commit()
        return render_template('index.html')
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        password=hashfunc(request.form["password"])
        con = sqlite3.connect('databaseforwebapp.db')
        row = con.execute("SELECT password FROM user WHERE email=trim(?)",(email,))#trim function removes extra spaces
        dbpass = row.fetchone()
        print(dbpass[0] == password)
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)