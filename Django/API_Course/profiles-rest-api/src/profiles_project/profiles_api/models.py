from django.db import models
from django.contrib.auth.models import AbstractBaseUser                         # Base of the standard Django user model, we build on top of it and add stuff to it
from django.contrib.auth.models import PermissionsMixin                         # Allows us to add permissions to our user model, let's us set permissions for users on the system
from django.contrib.auth.models import BaseUserManager                          # Helps us create our UserProfileManager

class UserProfileManager(BaseUserManager):
    """Helps Django work wirh our custom user model"""

    def create_user(self, email, name, password):
        """Creates a new user profile object"""
        if not email:                                                           # Checks that user provided an email
            raise ValueError('Users must have an email address.')
        email = self.normalize_email(email)                                     # Normalizes an email - lowercase
        user = self.model(email=email, name=name)                               # Creates a new user object
        user.set_password(password)                                             # Sets the password in the object
        user.save(using=self._db)                                               # Saves the user
        return user                                                             # Returns the user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details"""

        user = self.create_user(email, name, password)                          # Creates a standard user
        user.is_superuser = True                                                # Creates the admin variable
        user.is_staff = True
        user.save(using=self.db)                                                # Saves
        return user                                                             # Returns

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a "user proflie" inside our system."""                        # Doc string so other developers know what we're doing

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)                               # Determine whether this particular user is active in the system - Useful to disable user accounts - Required when a custome user is added in Django
    is_staff = models.BooleanField(default=False)                               # Determine whether a user is part of the staff(adming) - also required by the Django user model

    objects = UserProfileManager()                                              # Object Manager

    USERNAME_FIELD = 'email'                                                    # What the user uses to login
    REQUIRED_FIELDS = ['name']                                                  # Email is required by the system since it is used as the username

    def get_full_name(self):                                                    # Required by django admin
        """Used to get a users full name"""
        return self.name

    def get_short_name(self):
        """Used to get a users short name"""
        return self.name

    def __str__(self):                                                          # Function returns the object as a string
        """Django uses this when it needs to convert the object to a string"""
        return self.email
