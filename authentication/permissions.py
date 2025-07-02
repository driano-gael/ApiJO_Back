from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsAdminOrAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role == 'admin':
            return True
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return False

class IsAdminOrEmploye(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ('admin', 'employe')
