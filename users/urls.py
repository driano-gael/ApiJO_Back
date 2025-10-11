from django.urls import path

from users.models import EmployeProfile
from users.views import ClientListView
from users.views.client import ClientSetInactiveView
from users.views.employe import EmployeListView, EmployeSetInactiveView

urlpatterns = [

    path('client/', ClientListView.as_view(), name='clients-list'),

    path('setInactive/<int:pk>/', ClientSetInactiveView.as_view(), name='set-client-inactive'),

    path('employe/', EmployeListView.as_view(), name='employe-list'),

    path('setEmployeeInactive/<int:pk>/', EmployeSetInactiveView.as_view(), name='set-employee-inactive'),
]