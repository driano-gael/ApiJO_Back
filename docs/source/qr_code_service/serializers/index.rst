Serializers QR Code Service
============================

Le module qr_code_service contient des sérialiseurs pour la conversion des données QR code.

QRCodeSerializer
----------------

.. autoclass:: qr_code_service.serializers.QRCodeSerializer
   :members:
   :undoc-members:
   :show-inheritance:

**Description**
   Sérialiseur principal pour le modèle QrCode. Permet la conversion entre les objets
   QrCode et leur représentation JSON pour les échanges via l'API REST.

**Champs inclus**
   - **id** : Identifiant unique du QR code
   - **data** : Données encodées du QR code (image base64)
   - **ticket** : Informations complètes du ticket associé (lecture seule)
   - **ticket_id** : ID du ticket pour la création (écriture seule)

**Relations**
   - **ticket** : Utilise TicketSerializer pour afficher les détails complets du ticket
   - **ticket_id** : Champ d'écriture pour associer un ticket lors de la création

**Utilisation**
   Utilisé dans les vues API pour sérialiser les réponses contenant des QR codes
   et désérialiser les requêtes de création de QR codes.

TicketIdSerializer
------------------

.. autoclass:: qr_code_service.serializers.TicketIdSerializer
   :members:
   :undoc-members:
   :show-inheritance:

**Description**
   Sérialiseur simple pour valider les requêtes contenant uniquement un ID de ticket.

**Champs**
   - **ticket_id** (IntegerField) : ID du ticket à traiter

**Utilisation**
   Utilisé pour valider les données d'entrée dans les vues qui requièrent
   uniquement un identifiant de ticket, notamment pour la génération de QR codes.
