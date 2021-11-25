from flask import Flask, render_template, request
from werkzeug.utils import redirect
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        email=request.form["email"]
        password=request.form["password"]
        print(email,password)
        return render_template('index.html')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)