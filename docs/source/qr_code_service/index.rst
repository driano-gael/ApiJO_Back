Module QR Code Service
=====================

Le module qr_code_service gère la génération et la validation des codes QR pour les tickets dans l'API ApiJO.

Structure du module
------------------

.. toctree::
   :maxdepth: 2
   :caption: Composants du module QR Code Service:

   models/index
   views/index
   serializers/index

Description
-----------

Le module qr_code_service permet de :

- Générer des codes QR uniques pour chaque ticket
- Stocker les données des QR codes en base
- Valider les tickets via leur clé QR
- Contrôler l'accès aux tickets selon les permissions utilisateur

Fonctionnalités principales
-------------------------

**Génération de QR codes**
   Création automatique de codes QR basés sur la clé unique du ticket.

**Validation de tickets**
   Vérification de l'authenticité des tickets via leur code QR.

**Gestion des permissions**
   Contrôle d'accès selon le rôle (client pour ses propres tickets, employé pour validation).

**Stockage sécurisé**
   Sauvegarde des données QR en base de données avec relation OneToOne au ticket.

API Endpoints
-------------

Le module expose les endpoints suivants :

- ``POST /qr-code/`` - Génération d'un QR code pour un ticket
- ``GET /ticket/{key}/`` - Récupération d'un ticket par sa clé QR
