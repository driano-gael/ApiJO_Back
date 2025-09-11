from django.urls import path
from api.views.lieu import *
from api.views.discipline import *
from api.views.epreuve import *
from api.views.evenement import *
from api.views.offre import *

urlpatterns = [

    #LIEU
    path('lieu/', LieuListView.as_view(), name='lieu-list'),
    path('lieu/<int:pk>/', LieuDetailView.as_view(), name='lieu-detail'),
    path('lieu/create/', LieuCreateView.as_view(), name='lieu-create'),
    path('lieu/update/<int:pk>/', LieuUpdateView.as_view(), name='lieu-update'),
    path('lieu/delete/<int:pk>/', LieuDeleteView.as_view(), name='lieu-delete'),

    #DISCIPLINE
    path('discipline/', DisciplineListView.as_view(), name='discipline-list'),
    path('discipline/<int:pk>/', DisciplineDetailView.as_view(), name='discipline-detail'),
    path('discipline/create/', DisciplineCreateView.as_view(), name='discipline-create'),
    path('discipline/update/<int:pk>/', DisciplineUpdateView.as_view(), name='discipline-update'),
    path('discipline/delete/<int:pk>/', DisciplineDeleteView.as_view(), name='discipline-delete'),

    #EPREUVE
    path('epreuve/', EpreuveListView.as_view(), name='epreuve-list'),
    path('epreuve/<int:pk>/', EpreuveDetailView.as_view(), name='epreuve-detail'),
    path('epreuve/create/', EpreuveCreateView.as_view(), name='epreuve-create'),
    path('epreuve/update/<int:pk>/', EpreuveUpdateView.as_view(), name='epreuve-update'),
    path('epreuve/delete/<int:pk>/', EpreuveDeleteView.as_view(), name='epreuve-delete'),

    #EVENEMENT
    path('evenement/', EvenementListView.as_view(), name='evenement-list'),
    path('evenement/<int:pk>/', EvenementDetailView.as_view(), name='evenement-detail'),
    path('evenement/by-epreuve/<int:pk>/', EvenementByEpreuveView.as_view(), name='evenement-by-epreuve'),
    path('evenement/create/', EvenementCreateView.as_view(), name='evenement-create'),
    path('evenement/update/<int:pk>/', EvenementUpdateView.as_view(), name='evenement-update'),
    path('evenement/delete/<int:pk>/', EvenementDeleteView.as_view(), name='evenement-delete'),

    # OFFRE
    path('offre/', OffreListView.as_view(), name='offre-list'),
    path('offre/<int:pk>/', OffreDetailView.as_view(), name='offre-detail'),
    path('offre/create/', OffreCreateView.as_view(), name='offre-create'),
    path('offre/update/<int:pk>/', OffreUpdateView.as_view(), name='offre-update'),
    path('offre/delete/<int:pk>/', OffreDeleteView.as_view(), name='offre-delete'),
]