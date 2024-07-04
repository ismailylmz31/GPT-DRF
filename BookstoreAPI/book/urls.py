from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, logout, register
from .views import AdminView, AdminOrAssistantView, UserView
router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('admin-only/', AdminView.as_view(), name='admin-only'),
    path('admin-or-assistant/', AdminOrAssistantView.as_view(), name='admin-or-assistant'),
    path('user/', UserView.as_view(), name='user'),
]
