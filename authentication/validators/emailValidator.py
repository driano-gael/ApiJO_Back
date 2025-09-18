"""
Validateur personnalisé pour les adresses email.

Ce module contient un validateur qui vérifie non seulement le format de l'email,
mais aussi qu'il ne s'agit pas d'un email jetable et qu'il n'est pas déjà utilisé.
"""

import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from users.models.base_user import User  # adapte ce chemin selon ton projet

class EmailValidator:
    """
    Validateur personnalisé pour les adresses email.

    Vérifie le format de l'email, rejette les domaines d'emails jetables
    et s'assure que l'email n'est pas déjà enregistré dans le système.

    Attributes:
        forbidden_domains (list): Liste des domaines d'emails jetables interdits
    """

    def __init__(self, forbidden_domains=None):
        """
        Initialise le validateur avec une liste de domaines interdits.

        Args:
            forbidden_domains (list, optional): Domaines d'emails jetables à interdire.
                                               Utilise une liste par défaut si None.
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

        Args:
            value (str): L'adresse email à valider

        Raises:
            ValidationError: Si l'email n'est pas valide, est jetable ou déjà utilisé
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

        Returns:
            str: Message d'aide expliquant les règles de validation
        """
        return _(
            "Utilisez une adresse e-mail valide, non temporaire, et qui n'est pas déjà enregistrée."
        )
