from rest_framework import permissions


class AdminOnlyPermission(permissions.BasePermission):
    """
    Custom permission class that allows only admin users to update, delete, put, and read.
    Other users can only perform read operations.
    """

    def has_permission(self, request, view):
        # Allow read operations for all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow update, delete, put operations only for admin users
        return request.user and request.user.is_staff
