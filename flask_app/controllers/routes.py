from flask_app import app
from flask import redirect,render_template,request

#create post route for voting 

@app.route('/')
def index():
    return render_template('index.html')