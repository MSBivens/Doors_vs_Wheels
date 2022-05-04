from flask_app import app
from flask import redirect,render_template,request
from flask_app.models.user import User
from flask_app.models.door import Door
from flask_app.models.wheel import Wheel
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#create post route for voting 

@app.route('/')
def index():
    return render_template('landing_page.html')