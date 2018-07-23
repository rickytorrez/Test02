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
        connection = sqlite3.connect('data.db')                                         # Initialize the connection
        cursor = connection.cursor()                                                    # Initialize the cursor

        query = "SELECT * FROM users WHERE username=?"                                  # Query that will search the table for a given username
        result = cursor.execute(query, (username,))                                     # Get the result set for that found username
        row = result.fetchone()                                                         # Get the first row
        if row:                                                                         # If the row exists
            user = cls(*row)                                                            # Create a User object with the data from that row
                                                                                        # *row is a set of arguments for id, username and password
        else:                                                                           # If there's no row
            user = None                                                                 # user is none

        connection.close()                                                              # Close the connection
        return user                                                                     # return user or none

################################################ FIND USER BY USE ID #################################################
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')                                         # Initialize the connection
        cursor = connection.cursor()                                                    # Initialize the cursor

        query = "SELECT * FROM users WHERE id=?"                                        # Query that will search the table for a given id
        result = cursor.execute(query, (_id,))                                          # Get the result set for that found _id
        row = result.fetchone()                                                         # Get the first row
        if row:                                                                         # If the row exists
            user = cls(*row)                                                            # Create a User object with the data from that row
                                                                                        # *row is a set of arguments for id, username and password
        else:                                                                           # If there's no row
            user = None                                                                 # user is none

        connection.close()                                                              # Close the connection
        return user
