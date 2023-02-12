from flask import current_app
from flask import render_template

app = current_app

@app.route('/')
@app.route("/home")
@app.route("/index")
def index():
    return render_template('index.html')