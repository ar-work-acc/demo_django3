from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a Snippet to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message = 'Only the owner of the snippet can modify it.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
