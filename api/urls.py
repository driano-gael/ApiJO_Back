from django.urls import path
from .views import LieuListAPIView, LieuDetailAPIView, DisciplineListAPIView, DisciplineDetailAPIView

urlpatterns = [
    path('lieu/', LieuListAPIView.as_view(), name='lieu-list'),
    path('lieu/<int:pk>/', LieuDetailAPIView.as_view(), name='lieu-detail'),
    path('discipline/', DisciplineListAPIView.as_view(), name='discipline-list'),
    path('discipline/<int:pk>/', DisciplineDetailAPIView.as_view(), name='discipline-detail'),
]