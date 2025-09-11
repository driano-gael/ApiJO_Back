import rest_framework.generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.evenement import Evenement
from api.models.epreuve import Epreuve
from api.serializers.evenement import EvenementSerializer
from authentication.permissions import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class EvenementListView(rest_framework.generics.ListAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [AllowAny]

class EvenementDetailView(rest_framework.generics.RetrieveAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [AllowAny]

class EvenementByEpreuveView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        epreuve_id = kwargs.get('pk')
        epreuve = get_object_or_404(Epreuve, id=epreuve_id)
        evenement = epreuve.evenement
        if evenement is None:
            return Response({"detail": "Aucun événement associé à cette épreuve."}, status=404)
        serializer = EvenementSerializer(evenement)
        return Response(serializer.data)


class EvenementCreateView(rest_framework.generics.CreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class EvenementUpdateView(rest_framework.generics.UpdateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class EvenementDeleteView(rest_framework.generics.DestroyAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAuthenticated, IsAdmin]