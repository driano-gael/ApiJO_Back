Vue Employee
============

.. automodule:: authentication.views.employe
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

La vue **EmployeeRegisterView** permet aux administrateurs de créer des comptes employé.

EmployeeRegisterView
===================

**Endpoint :** ``POST /auth/register/employe/``

**Type :** ``generics.CreateAPIView``

**Permissions :** ``IsAdminUser`` (admin uniquement)

Fonctionnalités
===============

Création contrôlée
~~~~~~~~~~~~~~~~~

- Réservée aux administrateurs authentifiés
- Processus d'inscription supervisé pour le personnel
- Validation des données professionnelles

Données professionnelles
~~~~~~~~~~~~~~~~~~~~~~~

- Gestion du matricule employé unique
- Identifiant téléphonique professionnel
- Création automatique du profil EmployeProfile

Processus de création
====================

1. **Authentification** obligatoire de l'administrateur
2. **Réception** des données employé (email, password, nom, prenom, matricule, identifiant_telephone)
3. **Validation** via EmployeeRegisterSerializer
4. **Création** de l'utilisateur avec rôle 'employe'
5. **Génération** automatique du profil EmployeProfile
6. **Retour** du profil employé créé

Exemple d'utilisation
====================

.. code-block:: bash

   # Création d'un employé (admin requis)
   POST /auth/register/employe/
   Authorization: Bearer <admin_jwt_token>
   Content-Type: application/json

   {
     "email": "nouvel.employe@jeux-olympiques.fr",
     "password": "MotDePasseSecure123!",
     "nom": "Martin",
     "prenom": "Pierre",
     "matricule": "EMP002",
     "identifiant_telephone": "TEL-JO-2024-002"
   }

**Réponse de succès :**

.. code-block:: json

   {
     "id": 1,
     "user": {
       "id": 2,
       "email": "nouvel.employe@jeux-olympiques.fr",
       "role": "employe"
     },
     "nom": "Martin",
     "prenom": "Pierre",
     "matricule": "EMP002",
     "identifiant_telephone": "TEL-JO-2024-002"
   }

Gestion des erreurs
==================

**Erreurs d'authentification :**

.. code-block:: json

   {
     "detail": "Authentication credentials were not provided."
   }

**Erreurs de validation :**

.. code-block:: json

   {
     "email": ["Un utilisateur avec cet email existe déjà."],
     "matricule": ["Ce matricule est déjà utilisé."]
   }

Sécurité
========

- **Authentification obligatoire** avec token JWT valide
- **Vérification du rôle admin** avant autorisation
- **Validation stricte** des données professionnelles
- **Audit trail** des créations d'employés
