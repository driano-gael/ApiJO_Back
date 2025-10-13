Modèles QR Code Service
=======================

Le module qr_code_service contient un modèle principal pour la gestion des codes QR.

QrCode
------

.. autoclass:: qr_code_service.models.QrCode
   :members:
   :undoc-members:
   :show-inheritance:

**Description**
   Modèle représentant un code QR associé à un ticket. Chaque ticket peut avoir un code QR unique
   pour permettre sa validation lors des événements.

**Relations**
   - **ticket** (OneToOneField) : Relation unique vers le modèle Ticket
   - Chaque ticket peut avoir exactement un code QR
   - La suppression d'un ticket supprime automatiquement son code QR (CASCADE)

**Champs principaux**
   - **data** (TextField) : Données encodées du QR code (image base64)
   - **ticket** (OneToOneField) : Référence vers le ticket associé
   - **create_at** (DateTimeField) : Date de création automatique

**Méthodes**
   - **__str__()** : Retourne une représentation textuelle du QR code

**Utilisation**
   Ce modèle est utilisé pour stocker les données des codes QR générés automatiquement
   lors de la demande de génération par un client authentifié.
