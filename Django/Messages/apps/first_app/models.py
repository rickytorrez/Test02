from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

## UserManager can be viewed as validation ##
class UserManager(models.Manager):
    def register(self, first, last, username, email, dob, password, confirm):
        response = {
            "valid": True,
            "errors":[],
            "user": None
        }

        ## Validations ##
        if len(first) < 1:
            response["errors"].append("Please provide a first name")
        elif len(first) < 2:
            response["errors"].append("First name must be two characters or longer")

        if len(last) < 1:
            response["errors"].append("Please provide a last Name")
        elif len(last) < 2:
            response["errors"].append("Last name must be two characters or longer")

        if len(username) < 1:
            response["errors"].append("Please provide a username")
        elif len(username) < 2:
            response["errors"].append("Username must be two characters or longer")

        if len(email) < 1:
            response["errors"].append("Please provide an email")
        elif not EMAIL_REGEX.match(email):
            response["errors"].append("Invalid email")
        else: 
            email_list = User.objects.filter(email=email.lower())
            if len(email_list) > 0:
                response["errors"].append("Email is already in use")

        if len(dob) < 1:
            response["errors"].append("Date of birth is required")
        else:
            date = datetime.strptime(dob, '%Y-%m-%d')
            today = datetime.now()
            if date > today:
                response["errors"].append("Date of birth must be in the past")

        if len(password) < 1:
            response["errors"].append("A password is required")
        elif len(password) < 8:
            response["errors"].append("Password must be eight characters or longer")

        if len(confirm) < 3:
            response["errors"].append("Please confirm your password")
        elif confirm != password:
            response["errors"].append("Confirmed password must match password")
        print ("helooooooooooooooooooooooooooo")
        print first, last, username, email, dob
        
        if len(response["errors"]) > 0:
            response["valid"] = False

        else:
            response["user"] = User.objects.create(
                first_name = first,
                last_name = last,
                username = username,
                email = email.lower(),
                dob = date,
                password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            )

        return response

    def login(self, email, password):
        response = {
            "valid": True,
            "errors":[],
            "user": None
        }

        ## Validations ##
        if len(email) < 1:
            response["errors"].append("Please provide an email")
        elif not EMAIL_REGEX.match(email):
            response["errors"].append("Invalid email")
        else: 
            email_list = User.objects.filter(email=email.lower())
            if len(email_list) == 0:
                response["errors"].append("Unknown email")

        if len(password) < 1:
            response["errors"].append("A password is required")
        elif len(password) < 8:
            response["errors"].append("Password must be eight characters or longer")

        if len(response["errors"]) == 0:
            hashed_pw = email_list[0].password
            if bcrypt.checkpw(password.encode(), hashed_pw.encode()):
                response["user"] = email_list[0]
            else:
                response["errors"].append("Incorrect Password")

        if len(response["errors"]) > 0:
            response["valid"] = False

        return response

class User(models.Model):
    first_name  = models.CharField(max_length=255)
    last_name   = models.CharField(max_length=255)
    username    = models.CharField(max_length=255)
    email       = models.CharField(max_length=255)
    password    = models.CharField(max_length=255)
    dob         = models.DateField()
    create_at   = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    objects     = UserManager() ## <== Required to get validations
