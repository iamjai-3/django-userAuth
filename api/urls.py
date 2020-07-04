from django.urls import path
from .views import RegisterApi
from .views import LoginApi
from knox import views as knox_views
urlpatterns = [
    path('api/register/', RegisterApi.as_view(), name='register'),
    path('api/login/', LoginApi.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]