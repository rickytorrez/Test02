from rest_framework import permissions                                          # Somewhat like Spring Security


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own proflie."""

    def has_object_permission(self, request, view, obj):                        # User Permissions
        """Check user is tyring to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:                          # Let's a user view another user profile if its in the SAFE_METHODS (GET)
            return True
                                                                                # If its not a SAFE_METHOD - PUT, PATCH, DELETE
        return obj.id == request.user.id                                        # Check if the user is updating their own profile by checking that the
                                                                                # object_id matches the user.id that is making the request
