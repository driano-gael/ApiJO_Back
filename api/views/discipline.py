import rest_framework.generics
from api.models.discipline import Discipline
from api.serializers.discipline import DisciplineSerializer
from authentication.permissions import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class DisciplineListView(rest_framework.generics.ListAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [AllowAny]

class DisciplineDetailView(rest_framework.generics.RetrieveAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [AllowAny]

class DisciplineCreateView(rest_framework.generics.CreateAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class DisciplineUpdateView(rest_framework.generics.UpdateAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class DisciplineDeleteView(rest_framework.generics.DestroyAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAuthenticated, IsAdmin]