from werkzeug.security import safe_str_cmp
from user import User

################################################### TABLE OF USERS ###################################################
users = [
    User(1,'bob','asdf')
]

####################################### INSTANCE WITH THE USERNAME AS THE KEY ########################################
username_mapping = {u.username: u for u in users}

######################################## INSTANCE WITH THE USE ID AS THE KEY #########################################
userid_mapping = {u.id: u for u in users}

########################################## FUNCTION TO AUTHENTICATE A USER ###########################################
def authenticate(username, password):
    user = username_mapping.get(username, None)                                                     # Sets the username to the variable user and returns none if there's no username match
    if user and safe_str_cmp(user.password, password):                                              # if user is found and the password matches
        return user                                                                                 # return the user

########################################## FUNCTION TO AUTHENTICATE A USER ###########################################
def identity(payload):                                                                              # Unique functionto Flask JWT
    user_id = payload['identity']                                                                   # Extract the user Id from the payload
    return userid_mapping.get(user_id, None)                                                        #