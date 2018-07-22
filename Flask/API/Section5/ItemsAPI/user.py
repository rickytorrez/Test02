import sqlite3
from flask_restful import Resource, reqparse

#################################################### USER ENTITY #####################################################
class User:
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

################################################# USER REGISTRATION ##################################################
class UserRegister(Resource):

####################################### JSON PARSER FOR USERNAME AND PASSWORD ########################################
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank"
    )

############################################ REGISTERS A USER INTO THE DB ############################################
    def post(self):
        data = UserRegister.parser.parse_args()                                         # Get the data from the JSON payload

        if User.find_by_username(data['username']):                                     # If the username alreqady exists
            return {"message": "A user with that username already exists"}, 400         # Send error message

        connection = sqlite3.connect('data.db')                                         # Connect to the sqlite
        cursor = connection.cursor()                                                    # Start the cursor
        query = "INSERT INTO users VALUES (NULL, ?, ?)"                                 # Create query where id is null since it will auto increment
        cursor.execute(query, (data['username'], data['password']))                     # Use cursor to execute the query - username and password must be a tuple
        connection.commit()                                                             # Commit changes to DB
        connection.close()                                                              # Close connection
        return {"message": "User created successfully."}, 201                           # Return message
