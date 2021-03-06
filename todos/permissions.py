from rest_framework import permissions

class IsAuthorOrNothing(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user