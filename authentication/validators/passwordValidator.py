# users/validators.py
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext

class StrongPasswordValidator:
    def validate(self, password, user=None):
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
        return gettext(
            "Le mot de passe doit contenir au moins 12 caractères, "
            "avec une majuscule, une minuscule, un chiffre et un caractère spécial."
        )
