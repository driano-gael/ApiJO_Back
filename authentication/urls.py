from django.urls import path
from authentication.views.client import ClientRegisterView
from authentication.views.employe import EmployeeRegisterView
from authentication.views.token import CustomTokenObtainPairView

urlpatterns = [
    path('register/client', ClientRegisterView.as_view(), name='register-client'),
    path('register/employe', EmployeeRegisterView.as_view(), name='register-employe'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
]