"""
Classes de permissions personnalisées pour l'API des Jeux Olympiques.

Ce module définit les permissions spécifiques selon les rôles des utilisateurs :
admin, employé et client, avec différents niveaux d'accès aux ressources.
"""
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Permission pour les administrateurs uniquement.

    Accorde l'accès uniquement aux utilisateurs authentifiés ayant le rôle 'admin'.
    Utilisée pour les opérations sensibles nécessitant les plus hauts privilèges.
    """
    def has_permission(self, request, view):
        """
        Vérifie si l'utilisateur a les permissions d'administrateur.

        Args:
            request: La requête HTTP
            view: La vue appelée

        Returns:
            bool: True si l'utilisateur est admin authentifié, False sinon
        """
        return request.user.is_authenticated and request.user.role == 'admin'

class IsAdminOrAuthenticatedReadOnly(BasePermission):
    """
    Permission pour admin (accès complet) ou utilisateurs authentifiés (lecture seule).

    Les administrateurs ont un accès complet, tandis que les autres utilisateurs
    authentifiés ne peuvent que consulter les données (GET, HEAD, OPTIONS).
    """
    def has_permission(self, request, view):
        """
        Vérifie les permissions selon le rôle et la méthode HTTP.

        Args:
            request: La requête HTTP
            view: La vue appelée

        Returns:
            bool: True si autorisé selon le rôle et la méthode, False sinon
        """
        if not request.user.is_authenticated:
            return False
        if request.user.role == 'admin':
            return True
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return False

class IsAdminOrEmploye(BasePermission):
    """
    Permission pour les administrateurs et employés uniquement.

    Accorde l'accès aux utilisateurs ayant les rôles 'admin' ou 'employe'.
    Exclut les clients des opérations nécessitant un statut professionnel.
    """
    def has_permission(self, request, view):
        """
        Vérifie si l'utilisateur est admin ou employé.

        Args:
            request: La requête HTTP
            view: La vue appelée

        Returns:
            bool: True si l'utilisateur est admin ou employé, False sinon
        """
        return request.user.role in ('admin', 'employe')
