from django.urls import path
from users.views import ClientListView
from users.views.client import ClientSetInactiveView

urlpatterns = [

    path('client/', ClientListView.as_view(), name='clients-list'),

    path('setInactive/<int:pk>/', ClientSetInactiveView.as_view(), name='set-client-inactive'),
]