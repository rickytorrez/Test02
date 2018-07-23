import sqlite3
from db import db

#################################################### USER ENTITY #####################################################
class UserModel(db.Model):                                                              # db.Model creates the mapping between the database
                                                                                        # and the objects
    __tablename__ = 'users'                                                             # Tell SQLAlchemy what the table name is

    id = db.Column(db.Integer, primary_key=True)                                        # Tell SQLAlchemy to create the id Column
    username = db.Column(db.String(80))                                                 # Create the username column
    password = db.Column(db.String(80))                                                 # Create the password column

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

############################################### FIND USER BY USERNAME ################################################
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()                           # Return the cls(UserModel), start the query builder
                                                                                        # Filter by username(table name) = username(argument)
                                                                                        # Return the first row and SQLAlchemy converts it into
                                                                                        # an object

################################################ FIND USER BY USE ID #################################################
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()                                      # Similar to the method above
