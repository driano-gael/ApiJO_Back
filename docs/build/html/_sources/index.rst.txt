.. ApiJO documentation master file, created by
   sphinx-quickstart on Thu Sep 18 14:52:30 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation de l'API des Jeux Olympiques
==========================================

Bienvenue dans la documentation complète de l'API ApiJO (Jeux Olympiques).

Cette API REST permet de gérer tous les aspects des Jeux Olympiques :

- **Gestion des événements sportifs** : disciplines, épreuves, événements et lieux
- **Système d'authentification** : inscription et connexion des utilisateurs avec gestion des rôles
- **Gestion des utilisateurs** : profils clients et employés
- **Système de paiement** : gestion des transactions et création automatique de tickets
- **Service QR Code** : génération et validation des codes QR pour les billets
- **Offres commerciales** : packages et billets

Architecture
------------

L'API est construite avec Django REST Framework et utilise :

- **Authentification JWT** avec rôles (client, employé, admin)
- **Base de données PostgreSQL** pour la persistance
- **Permissions granulaires** selon les rôles utilisateurs
- **Validation avancée** des données (emails, mots de passe sécurisés)
- **Système de paiement simulé** pour les transactions
- **Génération de QR codes** pour la validation des billets

.. toctree::
   :maxdepth: 1
   :caption: Modules de l'API

   api/index
   authentication/index
   users/index
   payment/index
   qr_code_service/index

.. toctree::
   :maxdepth: 1
   :caption: Guides

   guide/installation
   guide/configuration

Indices et tables
=================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
