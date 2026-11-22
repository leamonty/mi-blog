from django.contrib.auth import views as auth_views
from django.urls import path
from .views import RegistroView


app_name = 'usuarios'

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='usuarios/login.html'
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]