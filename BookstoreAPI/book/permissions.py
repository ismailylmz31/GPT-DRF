from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsAssistantUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Assistant').exists()

class IsAdminOrAssistant(BasePermission):
    def has_permission(self, request, view):
        return (request.user and request.user.is_staff) or \
               (request.user and request.user.groups.filter(name='Assistant').exists())
