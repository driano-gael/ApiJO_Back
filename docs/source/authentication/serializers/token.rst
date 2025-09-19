Sérialiseur Token JWT
====================

.. automodule:: authentication.serializers.token
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Le **CustomTokenObtainPairSerializer** étend le sérialiseur JWT standard pour enrichir la réponse d'authentification avec les informations utilisateur.

Fonctionnalités
===============

Authentification enrichie
~~~~~~~~~~~~~~~~~~~~~~~~~

- Valide les identifiants (email + mot de passe)
- Génère les tokens JWT standard (access + refresh)
- **Enrichit la réponse** avec le rôle et l'email utilisateur

Validation personnalisée
~~~~~~~~~~~~~~~~~~~~~~~

- Authentification par email au lieu de username
- Messages d'erreur en français
- Contrôles de sécurité renforcés

Réponse enrichie
===============

**Données retournées lors de l'authentification :**

- ``access`` : Token d'accès JWT
- ``refresh`` : Token de rafraîchissement JWT
- ``role`` : Rôle de l'utilisateur (client, employe, admin)
- ``email`` : Email de l'utilisateur authentifié

Validation des identifiants
===========================

La méthode ``validate()`` personnalisée :

1. **Extraction** des identifiants (email, password)
2. **Vérification de présence** des deux champs
3. **Authentification** via Django authenticate()
4. **Validation du type** d'utilisateur (CustomUser)
5. **Enrichissement** de la réponse JWT

Messages d'erreur
=================

- **Identifiants manquants** : "Email et mot de passe requis."
- **Identifiants incorrects** : "Identifiants invalides."

Utilisation
===========

**Endpoint d'authentification :**

.. code-block:: bash

   POST /auth/login/
   Content-Type: application/json

   {
     "email": "user@example.com",
     "password": "motdepasse"
   }

**Réponse d'authentification :**

.. code-block:: json

   {
     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
     "role": "client",
     "email": "user@example.com"
   }

Intégration frontend
===================

Les informations enrichies permettent au frontend de :

- **Stocker le rôle** pour adapter l'interface
- **Afficher l'email** dans l'interface utilisateur
- **Gérer les permissions** côté client
- **Personnaliser l'expérience** selon le rôle

Exemple d'utilisation
====================

.. code-block:: python

   # Utilisation dans une vue personnalisée
   from authentication.views.token import CustomTokenObtainPairView

   # Le sérialiseur est utilisé automatiquement par la vue
   class CustomTokenObtainPairView(TokenObtainPairView):
       serializer_class = CustomTokenObtainPairSerializer
