Vue Client
==========

.. automodule:: authentication.views.client
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

La vue **ClientRegisterView** permet l'inscription libre des nouveaux clients.

ClientRegisterView
==================

**Endpoint :** ``POST /auth/register/client/``

**Type :** ``generics.CreateAPIView``

**Permissions :** ``AllowAny`` (accès libre)

Fonctionnalités
===============

Inscription libre
~~~~~~~~~~~~~~~~

- Accessible à tous les utilisateurs (pas d'authentification requise)
- Permet aux nouveaux utilisateurs de créer un compte client
- Processus d'inscription simplifié pour les clients finaux

Validation automatique
~~~~~~~~~~~~~~~~~~~~~

- Utilise le ``ClientRegisterSerializer`` pour la validation
- Contrôles de sécurité : email anti-spam, mot de passe robuste
- Création automatique du profil client

Processus d'inscription
======================

1. **Réception** des données client (email, password, nom, prenom, telephone)
2. **Validation** via ClientRegisterSerializer
3. **Création** de l'utilisateur avec rôle 'client'
4. **Génération** automatique du profil ClientProfile
5. **Retour** de l'utilisateur créé

Exemple d'utilisation
====================

.. code-block:: bash

   # Inscription d'un nouveau client
   POST /auth/register/client/
   Content-Type: application/json

   {
     "email": "nouveau.client@example.com",
     "password": "MonMotDePasse123!",
     "nom": "Dupont",
     "prenom": "Marie",
     "telephone": "0123456789"
   }

**Réponse de succès :**

.. code-block:: json

   {
     "id": 1,
     "email": "nouveau.client@example.com",
     "role": "client"
   }

Gestion des erreurs
==================

**Erreurs de validation typiques :**

- Email déjà utilisé
- Mot de passe trop faible
- Nom/prénom trop courts
- Téléphone invalide
- Email jetable détecté

.. code-block:: json

   {
     "email": ["Cet email est déjà utilisé."],
     "password": ["Le mot de passe doit contenir au moins 12 caractères."]
   }

Utilisation côté client
======================

Cette vue est typiquement utilisée par :

- **Page d'inscription** du site web public
- **Application mobile** pour nouveaux utilisateurs
- **Formulaires d'inscription** en libre accès
