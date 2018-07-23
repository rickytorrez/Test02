from werkzeug.security import safe_str_cmp
from models.user import UserModel                                                                   # Import from the correct file

########################################## FUNCTION TO AUTHENTICATE A USER ###########################################
def authenticate(username, password):
    user = UserModel.find_by_username(username)                                                     # Looks in the database for the username
    if user and safe_str_cmp(user.password, password):                                              # if user is found and the password matches
        return user                                                                                 # return the user

########################################## FUNCTION TO AUTHENTICATE A USER ###########################################
def identity(payload):                                                                              # Unique functionto Flask JWT
    user_id = payload['identity']                                                                   # Extract the user Id from the payload
    return UserModel.find_by_id(user_id)                                                            # Retrieve the id using user_id
