from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# init the class
class Door:
    db = "doors_vs_wheels_db"
    def __init__(self,data):
        self.id = data['id']
        self.count = data['count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data["user_id"]

# allows user to save door count to db
    @classmethod
    def save(cls,data):
        query = "INSERT INTO door (count) VALUES (%(count)s);"
        return connectToMySQL(cls.db).query_db(query,data)

# validates user input for door count
# valid = at least 1 count, has not submitted before
    @staticmethod
    def is_valid(door):
        is_valid = True
        query = "SELECT * FROM door WHERE user_id = %(user_id)s;"
        results = connectToMySQL(Door.db).query_db(query,door)
        if len(door['count']) > 0:
            flash("Are you sure you don't have at least one door?", "door")
            is_valid = False
        if results.match(door['user_id']):
            flash("You have already submitted your door count", "door")
            is_valid = False
        return is_valid