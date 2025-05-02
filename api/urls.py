from django.urls import path
from .views import LieuListAPIView, LieuDetailAPIView

urlpatterns = [
    path('lieu/', LieuListAPIView.as_view(), name='lieu-list'),
    path('lieu/<int:pk>/', LieuDetailAPIView.as_view(), name='lieu-detail'),
]