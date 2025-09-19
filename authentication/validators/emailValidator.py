"""
Validateur personnalisé pour les adresses email.

Ce module fournit un validateur qui vérifie le format de l'email,
rejette les emails jetables et s'assure que l'adresse n'est pas déjà utilisée
dans le système.

:module: users.validators.email
"""

import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from users.models.base_user import User  # adapte ce chemin selon ton projet

class EmailValidator:
    """
    Validateur personnalisé pour les adresses email.

    Vérifie :
        - le format de l'email,
        - l'absence de domaines d'emails jetables,
        - l'unicité de l'email dans la base de données.

    :ivar forbidden_domains: Liste des domaines d'emails jetables interdits
    :type forbidden_domains: list
    """

    def __init__(self, forbidden_domains=None):
        """
        Initialise le validateur avec une liste de domaines interdits.

        :param forbidden_domains: Domaines d'emails jetables à interdire
        :type forbidden_domains: list, optional
        """
        self.forbidden_domains = forbidden_domains or [
            'tempmail.com',
            'mailinator.com',
            'yopmail.com',
            '10minutemail.com',
        ]

    def __call__(self, value):
        """
        Valide l'adresse email selon plusieurs critères.

        :param value: L'adresse email à valider
        :type value: str
        :raises ValidationError: Si l'email est invalide, jetable ou déjà utilisé
        """
        # Vérification du format
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
            raise ValidationError(_("Adresse e-mail invalide."))

        # Vérification des domaines interdits
        domain = value.split('@')[-1].lower()
        if domain in self.forbidden_domains:
            raise ValidationError(_("Les adresses e-mail jetables ne sont pas autorisées."))

        # Vérification de l'unicité
        if User.objects.filter(email__iexact=value).exists():
            raise ValidationError(_("Un utilisateur avec cet e-mail existe déjà."))

    def get_help_text(self):
        """
        Retourne le texte d'aide pour ce validateur.

        :return: Message d'aide expliquant les règles de validation
        :rtype: str
        """
        return _(
            "Utilisez une adresse e-mail valide, non temporaire, et qui n'est pas déjà enregistrée."
        )
