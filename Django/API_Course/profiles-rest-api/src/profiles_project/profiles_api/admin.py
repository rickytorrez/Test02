from django.contrib import admin
from . import models                                                            # From current location, import the models module

admin.site.register(models.UserProfile)                                         # Using the .register function pass the UserProfile model to create an admin
