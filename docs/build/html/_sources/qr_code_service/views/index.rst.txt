Vues QR Code Service
===================

Le module qr_code_service contient deux vues principales pour la gestion des codes QR.

QRCodeCreateByTicket
--------------------

.. autoclass:: qr_code_service.views.QRCodeCreateByTicket
   :members:
   :undoc-members:
   :show-inheritance:

**Description**
   Vue API pour créer ou récupérer un code QR associé à un ticket spécifique.

**Permissions**
   - Utilisateur authentifié requis
   - Le client ne peut générer des QR codes que pour ses propres tickets

**Endpoint**
   - **POST** ``/qr-code/`` - Génère un QR code pour un ticket donné

**Paramètres**
   - **ticket_id** (int) : ID du ticket pour lequel générer le QR code

**Réponses**
   - **200** : QR code existant retourné
   - **201** : Nouveau QR code créé avec succès
   - **400** : ticket_id manquant ou invalide
   - **403** : Accès non autorisé au ticket

**Comportement**
   1. Vérifie que le ticket appartient au client authentifié
   2. Retourne le QR code existant si déjà généré
   3. Sinon, génère un nouveau QR code basé sur la clé du ticket
   4. Stocke les données du QR code en base64 dans la base de données

TicketByKeyView
---------------

.. autoclass:: qr_code_service.views.TicketByKeyView
   :members:
   :undoc-members:
   :show-inheritance:

**Description**
   Vue API pour valider un ticket à partir de sa clé QR. Utilisée par les employés
   pour vérifier l'authenticité des billets lors des événements.

**Permissions**
   - Réservée aux employés et administrateurs authentifiés

**Endpoint**
   - **GET** ``/ticket/{key}/`` - Récupère les informations d'un ticket par sa clé

**Paramètres**
   - **key** (str) : Clé unique du ticket extraite du QR code

**Réponses**
   - **200** : Ticket trouvé et retourné avec toutes ses informations
   - **404** : Ticket introuvable (clé invalide ou ticket supprimé)

**Comportement**
   1. Recherche le ticket correspondant à la clé fournie
   2. Retourne toutes les informations du ticket si trouvé
   3. Permet aux employés de valider l'authenticité du billet
