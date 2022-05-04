from flask_app import app
from flask_app.controllers import doors, users, wheels


if __name__ == "__main__":
    app.run(debug=True)