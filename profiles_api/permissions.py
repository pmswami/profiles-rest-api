from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            # Allow safe methods like GET and HEAD
            return True
        return obj.id == request.user.id
        

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update thier own status"""

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id==request.user.id