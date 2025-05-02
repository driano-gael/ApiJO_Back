from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView, ListCreateAPIView

from .models import Lieu
from .serializers import LieuSerializer

class LieuListAPIView(ListCreateAPIView):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer

class LieuDetailAPIView(RetrieveAPIView):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer