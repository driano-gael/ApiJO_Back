Module Authentication - Système d'Authentification JWT
========================================================

Le module **Authentication** gère l'authentification des utilisateurs avec un système JWT basé sur les rôles.

Fonctionnalités
---------------

- **Inscription sécurisée** : Clients (libre) et employés (admin uniquement)
- **Authentification JWT** : Tokens avec informations de rôle intégrées
- **Validation avancée** : Emails anti-spam et mots de passe sécurisés
- **Permissions granulaires** : Contrôle d'accès basé sur les rôles


**Rôles disponibles :**
- **Client** : Utilisateurs finaux (inscription libre)
- **Employé** : Personnel autorisé (création par admin)
- **Admin** : Accès complet à toutes les fonctionnalités (compte fournis)

**Sécurité :**
- Mots de passe : 12 caractères min, majuscule, minuscule, chiffre, caractère spécial
- Emails : Validation anti-domaines jetables
- JWT : Tokens avec expiration configurable

.. toctree::
   :maxdepth: 2
   :caption: Composants du module Authentication

   serializers/index
   views/index
   validators/index
   permissions
