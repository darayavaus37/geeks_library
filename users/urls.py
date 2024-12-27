from django.urls import path
from . import views

app_name = 'users'  # Namespace приложения

urlpatterns = [
    path('login/', views.login_view, name='login'),  # URL для входа
    path('register/', views.register_view, name='register'),  # URL для регистрации
]
