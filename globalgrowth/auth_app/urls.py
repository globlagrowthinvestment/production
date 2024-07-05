from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    
]