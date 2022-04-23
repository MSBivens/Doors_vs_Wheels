from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# init the class
class Wheel:
    db = "doors_vs_wheels_db"
    def __init__(self,data):
        self.id = data['id']
        self.count = data['count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data["user_id"]

# allows user to save wheel count to db
    @classmethod
    def save(cls,data):
        query = "INSERT INTO wheel (count) VALUES (%(count)s);"
        return connectToMySQL(cls.db).query_db(query,data)

# validates user input for wheel count
# valid = at least 1 count, has not submitted before
    @staticmethod
    def is_valid(wheel):
        is_valid = True
        if len(wheel['count']) > 0:
            is_valid = False
            flash("Are you sure you don't have at least one wheel?")
        # TO DO validate the user has not submmitted a count before
        return is_valid