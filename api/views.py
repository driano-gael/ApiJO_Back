from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView, ListCreateAPIView

from .models import Lieu, Discipline
from .serializers import LieuSerializer, DisciplineSerializer

class LieuListAPIView(ListCreateAPIView):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer

class LieuDetailAPIView(RetrieveAPIView):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer

class DisciplineListAPIView(ListCreateAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

class DisciplineDetailAPIView(RetrieveAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer