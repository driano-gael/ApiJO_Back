from django.db import models
from .base_user import User


class AdminProfile(models.Model):
    """
    Modèle représentant le profil d'un administrateur.

    Ce profil est lié à un utilisateur via une relation OneToOne et contient
    des informations supplémentaires propres aux administrateurs.

    :ivar user: L'utilisateur associé au profil admin
    :vartype user: User
    :ivar nom: Nom de famille de l'administrateur
    :vartype nom: str
    :ivar prenom: Prénom de l'administrateur
    :vartype prenom: str
    :ivar matricule: Identifiant unique de l'administrateur
    :vartype matricule: str
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="admin_profile",
        help_text="Utilisateur lié à ce profil administrateur."
    )
    nom = models.CharField(
        max_length=100,
        help_text="Nom de famille de l'administrateur."
    )
    prenom = models.CharField(
        max_length=100,
        help_text="Prénom de l'administrateur."
    )
    matricule = models.CharField(
        max_length=50,
        unique=True,
        help_text="Matricule unique identifiant l'administrateur."
    )

    class Meta:
        """
        Métadonnées du modèle AdminProfile.

        :cvar verbose_name: Nom lisible du modèle au singulier
        :vartype verbose_name: str
        :cvar verbose_name_plural: Nom lisible du modèle au pluriel
        :vartype verbose_name_plural: str
        """
        verbose_name = "Profil administrateur"
        verbose_name_plural = "Profils administrateurs"

    def __str__(self):
        """
        Représentation textuelle du profil administrateur.

        :return: Prénom et nom de l'administrateur avec son matricule
        :rtype: str
        """
        return f"{self.prenom} {self.nom} (Matricule: {self.matricule})"
