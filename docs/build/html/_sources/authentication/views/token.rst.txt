Vue Token JWT
=============

.. automodule:: authentication.views.token
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

La vue **CustomTokenObtainPairView** gère l'authentification JWT avec réponse enrichie incluant le rôle utilisateur.

CustomTokenObtainPairView
========================

**Endpoint :** ``POST /auth/login/``

**Type :** ``TokenObtainPairView`` (JWT standard étendu)

**Permissions :** ``AllowAny`` (accès libre)

Fonctionnalités
===============

Authentification enrichie
~~~~~~~~~~~~~~~~~~~~~~~~

- Génère les tokens JWT standard (access + refresh)
- **Enrichit la réponse** avec le rôle et l'email utilisateur
- Facilite la gestion des permissions côté frontend

Authentification par email
~~~~~~~~~~~~~~~~~~~~~~~~~

- Utilise l'email comme identifiant (au lieu du username)
- Compatible avec le modèle utilisateur personnalisé
- Messages d'erreur en français

Réponse complète
===============

**Données retournées :**

- ``access`` : Token d'accès JWT (courte durée)
- ``refresh`` : Token de rafraîchissement JWT (longue durée)
- ``role`` : Rôle de l'utilisateur (client, employe, admin)
- ``email`` : Email de l'utilisateur authentifié

Exemple d'utilisation
====================

.. code-block:: bash

   # Connexion utilisateur
   POST /auth/login/
   Content-Type: application/json

   {
     "email": "user@example.com",
     "password": "motdepasse"
   }

**Réponse de succès :**

.. code-block:: json

   {
     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk...",
     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5...",
     "role": "client",
     "email": "user@example.com"
   }

Gestion des erreurs
==================

**Identifiants manquants :**

.. code-block:: json

   {
     "non_field_errors": ["Email et mot de passe requis."]
   }

**Identifiants incorrects :**

.. code-block:: json

   {
     "non_field_errors": ["Identifiants invalides."]
   }

Intégration frontend
===================

Les informations enrichies permettent au frontend de :

.. code-block:: javascript

   // Exemple d'utilisation côté client
   const response = await fetch('/auth/login/', {
     method: 'POST',
     headers: { 'Content-Type': 'application/json' },
     body: JSON.stringify({ email, password })
   });

   const data = await response.json();

   // Stocker les tokens
   localStorage.setItem('access_token', data.access);
   localStorage.setItem('refresh_token', data.refresh);

   // Adapter l'interface selon le rôle
   if (data.role === 'admin') {
     showAdminPanel();
   } else if (data.role === 'employe') {
     showEmployeeFeatures();
   }

Endpoint de rafraîchissement
===========================

**Endpoint :** ``POST /auth/refresh/``

Utilise le token de rafraîchissement pour obtenir un nouveau token d'accès :

.. code-block:: bash

   POST /auth/refresh/
   Content-Type: application/json

   {
     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
   }

Configuration JWT
================

Les durées de vie des tokens sont configurées dans ``settings.py`` :

- **ACCESS_TOKEN_LIFETIME** : Durée du token d'accès
- **REFRESH_TOKEN_LIFETIME** : Durée du token de rafraîchissement
