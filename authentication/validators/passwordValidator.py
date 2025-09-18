"""
Validateur personnalisé pour les mots de passe forts.

Ce module contient un validateur qui impose des règles strictes pour les mots de passe :
- Minimum 12 caractères
- Au moins une majuscule, une minuscule, un chiffre et un caractère spécial
"""

import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext

class StrongPasswordValidator:
    """
    Validateur pour des mots de passe sécurisés.

    Impose des règles strictes de sécurité pour les mots de passe utilisateur :
    - Longueur minimale de 12 caractères
    - Présence obligatoire d'au moins une majuscule
    - Présence obligatoire d'au moins une minuscule
    - Présence obligatoire d'au moins un chiffre
    - Présence obligatoire d'au moins un caractère spécial
    """

    def validate(self, password, user=None):
        """
        Valide un mot de passe selon les règles de sécurité définies.

        Args:
            password (str): Le mot de passe à valider
            user (User, optional): L'utilisateur associé (non utilisé ici)

        Raises:
            ValidationError: Si le mot de passe ne respecte pas une des règles
        """
        if len(password) < 12:
            raise ValidationError(gettext("Le mot de passe doit contenir au moins 12 caractères."))

        if not re.search(r'[A-Z]', password):
            raise ValidationError(gettext("Le mot de passe doit contenir au moins une majuscule."))

        if not re.search(r'[a-z]', password):
            raise ValidationError(gettext("Le mot de passe doit contenir au moins une minuscule."))

        if not re.search(r'[0-9]', password):
            raise ValidationError(gettext("Le mot de passe doit contenir au moins un chiffre."))

        if not re.search(r'[^A-Za-z0-9]', password):
            raise ValidationError(gettext("Le mot de passe doit contenir au moins un caractère spécial."))

    def get_help_text(self):
        """
        Retourne le texte d'aide pour ce validateur.

        Returns:
            str: Message d'aide expliquant les règles de mot de passe
        """
        return gettext(
            "Le mot de passe doit contenir au moins 12 caractères, "
            "avec une majuscule, une minuscule, un chiffre et un caractère spécial."
        )
