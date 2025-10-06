from rest_framework import serializers

from qr_code_service.models import QrCode


class QRCodeSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle QRCode.

    Permet la conversion entre les objets QRCode et leur représentation JSON
    pour les échanges via l'API REST. Inclut tous les champs du modèle.

    Attributes:
        code (str): Contenu du QR code
        created_at (datetime): Date et heure de création du QR code
        updated_at (datetime): Date et heure de la dernière mise à jour du QR code
    """
    class Meta:
        """
        Configuration du sérialiseur.

        Attributes:
            model (Model): Modèle Django associé au sérialiseur
            fields (str): Champs inclus dans la sérialisation
        """
        model = QrCode
        fields = '__all__'
