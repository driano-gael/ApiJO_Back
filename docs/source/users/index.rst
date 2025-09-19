Module Users - Gestion des Utilisateurs
=======================================

Le module **Users** gère les modèles d'utilisateurs et profils avec un système personnalisé basé sur l'email.

Architecture utilisateur
------------------------

**Modèle de base personnalisé :**
- **User** : Modèle d'utilisateur basé sur l'email (remplace le User Django standard)
- **UserManager** : Gestionnaire personnalisé pour création d'utilisateurs par rôle

**Profils spécialisés :**
- **ClientProfile** : Profil client avec clé chiffrée automatique
- **EmployeProfile** : Profil employé avec matricule et identifiants professionnels

Fonctionnalités clés
--------------------

- **Email comme identifiant** : Pas de username, utilisation de l'email unique
- **Système de rôles** : client, employe, admin avec permissions granulaires
- **Profils automatiques** : Création automatique selon le rôle utilisateur
- **Sécurité renforcée** : Clés chiffrées, matricules uniques

.. toctree::
   :maxdepth: 2
   :caption: Composants du module Users

   models/index
   serializers/index
   managers
