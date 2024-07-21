from rest_framework import permissions

class UserOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admins to access it.
    """
    def has_permission(self, request, view):
        # Allow access if the user is an admin
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Allow access if the user is an admin or the owner of the object
        return request.user and (request.user.is_staff or obj.user == request.user)
