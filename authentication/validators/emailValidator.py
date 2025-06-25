import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from users.models.base_user import User  # adapte ce chemin selon ton projet

class EmailValidator:
    def __init__(self, forbidden_domains=None):
        self.forbidden_domains = forbidden_domains or [
            'tempmail.com',
            'mailinator.com',
            'yopmail.com',
            '10minutemail.com',
        ]

    def __call__(self, value):

        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
            raise ValidationError(_("Adresse e-mail invalide."))

        domain = value.split('@')[-1].lower()
        if domain in self.forbidden_domains:
            raise ValidationError(_("Les adresses e-mail jetables ne sont pas autorisées."))

        if User.objects.filter(email__iexact=value).exists():
            raise ValidationError(_("Un utilisateur avec cet e-mail existe déjà."))

    def get_help_text(self):
        return _(
            "Utilisez une adresse e-mail valide, non temporaire, et qui n’est pas déjà enregistrée."
        )
