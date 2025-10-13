Module Payment
==============

Le module payment gère les transactions de paiement et la création de tickets dans l'API ApiJO.

Structure du module
------------------

.. toctree::
   :maxdepth: 2
   :caption: Composants du module Payment:

   views/index
   serializers/index
   services/index
   infrastructure/index

Description
-----------

Le module payment simule un système de paiement complet avec :

- Création d'intentions de paiement
- Confirmation des transactions
- Gestion des remboursements
- Création automatique de tickets après paiement réussi

Fonctionnalités principales
-------------------------

**Simulation de paiement**
   Système mock pour tester les transactions sans vraie passerelle de paiement.

**Gestion des paniers**
   Traitement des items de panier pour créer des tickets correspondants.

**Gestion des places**
   Vérification automatique de la disponibilité des places avant création de tickets.

**Transactions atomiques**
   Utilisation des transactions Django pour garantir la cohérence des données.
