import rest_framework.generics
from django.db.models import Q
from api.models.discipline import Discipline
from api.serializers.discipline import DisciplineSerializer
from authentication.permissions import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class DisciplineListView(rest_framework.generics.ListAPIView):
    serializer_class = DisciplineSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Discipline.objects.all()
        search = self.request.GET.get('search', None)
        if search is not None:
            queryset = queryset.filter(
                Q(nom__istartswith=search)
            )
        return queryset.order_by('nom')

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