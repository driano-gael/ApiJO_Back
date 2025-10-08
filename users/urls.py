from django.urls import path
from users.views import ClientListView

urlpatterns = [

    path('client/', ClientListView.as_view(), name='clients-list'),
]