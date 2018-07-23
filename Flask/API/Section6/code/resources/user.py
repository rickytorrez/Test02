import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

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

        if UserModel.find_by_username(data['username']):                                # If the username alreqady exists
            return {"message": "A user with that username already exists"}, 400         # Send error message

        connection = sqlite3.connect('data.db')                                         # Connect to the sqlite
        cursor = connection.cursor()                                                    # Start the cursor
        query = "INSERT INTO users VALUES (NULL, ?, ?)"                                 # Create query where id is null since it will auto increment
        cursor.execute(query, (data['username'], data['password']))                     # Use cursor to execute the query - username and password must be a tuple
        connection.commit()                                                             # Commit changes to DB
        connection.close()                                                              # Close connection
        return {"message": "User created successfully."}, 201                           # Return message
