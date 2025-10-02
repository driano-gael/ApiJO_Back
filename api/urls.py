"""
Configuration des URLs de l'API des Jeux Olympiques.

Ce module définit toutes les routes de l'API REST pour la gestion des entités
des Jeux Olympiques : lieux, disciplines, épreuves, événements et offres.

Patterns d'URL disponibles :
- /lieu/ : CRUD pour les lieux sportifs
- /discipline/ : CRUD pour les disciplines sportives avec recherche
- /epreuve/ : CRUD pour les épreuves
- /evenement/ : CRUD pour les événements + récupération par épreuve
- /offre/ : CRUD pour les offres commerciales
"""

from django.urls import path
from api.views.lieu import *
from api.views.discipline import *
from api.views.epreuve import *
from api.views.evenement import *
from api.views.offre import *
from api.views.ticket import *

urlpatterns = [
    # LIEU - Gestion des lieux sportifs
    path('lieu/', LieuListView.as_view(), name='lieu-list'),
    path('lieu/<int:pk>/', LieuDetailView.as_view(), name='lieu-detail'),
    path('lieu/create/', LieuCreateView.as_view(), name='lieu-create'),
    path('lieu/update/<int:pk>/', LieuUpdateView.as_view(), name='lieu-update'),
    path('lieu/delete/<int:pk>/', LieuDeleteView.as_view(), name='lieu-delete'),

    # DISCIPLINE - Gestion des disciplines sportives
    path('discipline/', DisciplineListView.as_view(), name='discipline-list'),
    path('discipline/<int:pk>/', DisciplineDetailView.as_view(), name='discipline-detail'),
    path('discipline/create/', DisciplineCreateView.as_view(), name='discipline-create'),
    path('discipline/update/<int:pk>/', DisciplineUpdateView.as_view(), name='discipline-update'),
    path('discipline/delete/<int:pk>/', DisciplineDeleteView.as_view(), name='discipline-delete'),

    # EPREUVE - Gestion des épreuves
    path('epreuve/', EpreuveListView.as_view(), name='epreuve-list'),
    path('epreuve/<int:pk>/', EpreuveDetailView.as_view(), name='epreuve-detail'),
    path('epreuve/create/', EpreuveCreateView.as_view(), name='epreuve-create'),
    path('epreuve/update/<int:pk>/', EpreuveUpdateView.as_view(), name='epreuve-update'),
    path('epreuve/delete/<int:pk>/', EpreuveDeleteView.as_view(), name='epreuve-delete'),

    # EVENEMENT - Gestion des événements
    path('evenement/', EvenementListView.as_view(), name='evenement-list'),
    path('evenement/<int:pk>/', EvenementDetailView.as_view(), name='evenement-detail'),
    path('evenement/by-epreuve/<int:pk>/', EvenementByEpreuveView.as_view(), name='evenement-by-epreuve'),
    path('evenement/create/', EvenementCreateView.as_view(), name='evenement-create'),
    path('evenement/update/<int:pk>/', EvenementUpdateView.as_view(), name='evenement-update'),
    path('evenement/delete/<int:pk>/', EvenementDeleteView.as_view(), name='evenement-delete'),

    # OFFRE - Gestion des offres commerciales
    path('offre/', OffreListView.as_view(), name='offre-list'),
    path('offre/<int:pk>/', OffreDetailView.as_view(), name='offre-detail'),
    path('offre/create/', OffreCreateView.as_view(), name='offre-create'),
    path('offre/update/<int:pk>/', OffreUpdateView.as_view(), name='offre-update'),
    path('offre/delete/<int:pk>/', OffreDeleteView.as_view(), name='offre-delete'),

    path('ticket/', TicketListView.as_view(), name='ticket-list'),# Ticket
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('ticket/create/', TicketBatchCreateView.as_view(), name='tickets-create'),
]