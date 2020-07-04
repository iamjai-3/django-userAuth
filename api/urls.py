from django.urls import path, include
from .views import RegisterApi, LoginApi, ChangePasswordApi
from knox import views as knox_views

urlpatterns = [
    path('api/register/', RegisterApi.as_view(), name='register'),
    path('api/login/', LoginApi.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordApi.as_view(), name="change-password"),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]