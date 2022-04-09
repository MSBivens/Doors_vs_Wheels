from ..config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

# init the class
class Door:
    db = "doors_vs_wheels_db"
    def __init__(self,data):
        self.id = data['id']
        self.count = data['count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# allows user to save door count to db
    @classmethod
    def save(cls,data):
        query = "INSERT INTO door (count) VALUES (%(count)s);"
        return connectToMySQL(cls.db).query_db(query,data)

# validates user input for door count
    @staticmethod
    def is_valid(door):
        is_valid = True
        query = "SELECT * FROM door WHERE " #HELP
        count = connectToMySQL(Door.db).query_db(query,door)
        # validates the user is submitting a door count of at least 1
        if len(door['count']) > 0:
            is_valid = False
            flash("Are you sure you don't have at least one door?")
        return is_valid

# TO DO validate the user has not submmitted a count before