"""
Classes de permissions personnalisées pour l'API des Jeux Olympiques.

Ce module définit les permissions spécifiques selon les rôles des utilisateurs :
admin, employé et client, avec différents niveaux d'accès aux ressources.
"""

from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Permission pour les administrateurs uniquement.

    Accorde l'accès uniquement aux utilisateurs authentifiés ayant le rôle ``admin``.
    Utilisée pour les opérations sensibles nécessitant les plus hauts privilèges.
    """

    def has_permission(self, request, view):
        """
        Vérifie si l'utilisateur a les permissions d'administrateur.

        :param request: La requête HTTP
        :param view: La vue appelée
        :return: ``True`` si l'utilisateur est admin authentifié, sinon ``False``
        :rtype: bool
        """
        return request.user.is_authenticated and getattr(request.user, "role", None) == "admin"


class IsAdminOrAuthenticatedReadOnly(BasePermission):
    """
    Permission pour admin (accès complet) ou utilisateurs authentifiés (lecture seule).

    - Les administrateurs ont un accès complet.
    - Les autres utilisateurs authentifiés ne peuvent que consulter les données
      (méthodes ``GET``, ``HEAD``, ``OPTIONS``).
    """

    def has_permission(self, request, view):
        """
        Vérifie les permissions selon le rôle et la méthode HTTP.

        :param request: La requête HTTP
        :param view: La vue appelée
        :return: ``True`` si autorisé selon le rôle et la méthode, sinon ``False``
        :rtype: bool
        """
        if not request.user.is_authenticated:
            return False
        if getattr(request.user, "role", None) == "admin":
            return True
        return request.method in ("GET", "HEAD", "OPTIONS")


class IsAdminOrEmploye(BasePermission):
    """
    Permission pour les administrateurs et employés uniquement.

    Accorde l'accès aux utilisateurs authentifiés ayant les rôles
    ``admin`` ou ``employe``. Exclut les clients et utilisateurs anonymes.
    """

    def has_permission(self, request, view):
        """
        Vérifie si l'utilisateur est admin ou employé.

        :param request: La requête HTTP
        :param view: La vue appelée
        :return: ``True`` si l'utilisateur est admin ou employé, sinon ``False``
        :rtype: bool
        """
        return request.user.is_authenticated and getattr(request.user, "role", None) in ("admin", "employe")
