"""
Configuration des URLs de l'authentification.

Ce module définit toutes les routes liées à l'authentification :
- Inscription des clients et employés
- Connexion avec JWT
- Rafraîchissement des tokens
"""

from django.urls import path
from authentication.views.client import ClientRegisterView
from authentication.views.employe import EmployeeRegisterView
from rest_framework_simplejwt.views import TokenRefreshView
from authentication.views.token import CustomTokenObtainPairView

urlpatterns = [
    # Inscription des utilisateurs
    path('register/client/', ClientRegisterView.as_view(), name='register-client'),
    path('register/employe/', EmployeeRegisterView.as_view(), name='register-employe'),

    # Authentification JWT
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]