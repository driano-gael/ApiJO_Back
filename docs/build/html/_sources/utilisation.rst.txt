Utilisation
===========

Ce guide pratique vous montre comment utiliser l'API ApiJO pour gérer les Jeux Olympiques.

Démarrage rapide
================

Lancement du serveur
--------------------

.. code-block:: bash

   # Activation de l'environnement virtuel
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows

   # Démarrage du serveur
   python manage.py runserver

L'API sera accessible sur http://127.0.0.1:8000/

Authentification
================

Inscription d'un client
-----------------------

**Endpoint :** ``POST /auth/register/client/``

.. code-block:: json

   {
       "email": "client@example.com",
       "password": "MonMotDePasse123!",
       "nom": "Dupont",
       "prenom": "Jean",
       "telephone": "0123456789"
   }

**Réponse :**

.. code-block:: json

   {
       "id": 1,
       "email": "client@example.com",
       "role": "client",
       "profile": {
           "nom": "Dupont",
           "prenom": "Jean",
           "telephone": "0123456789",
           "cle_chiffre": "CLE_GENEREE_AUTOMATIQUEMENT"
       }
   }

Connexion
---------

**Endpoint :** ``POST /auth/login/``

.. code-block:: json

   {
       "email": "client@example.com",
       "password": "MonMotDePasse123!"
   }

**Réponse :**

.. code-block:: json

   {
       "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
       "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
       "user": {
           "id": 1,
           "email": "client@example.com",
           "role": "client"
       }
   }

Utilisation des tokens JWT
--------------------------

Incluez le token d'accès dans l'en-tête de vos requêtes :

.. code-block:: bash

   Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...

Gestion des événements sportifs
===============================

Consultation des disciplines
----------------------------

**Endpoint :** ``GET /api/disciplines/``

.. code-block:: json

   [
       {
           "id": 1,
           "nom": "Natation",
           "icone": "🏊‍♂️"
       },
       {
           "id": 2,
           "nom": "Athlétisme",
           "icone": "🏃‍♂️"
       }
   ]

Consultation des lieux
----------------------

**Endpoint :** ``GET /api/lieux/``

.. code-block:: json

   [
       {
           "id": 1,
           "nom": "Centre Aquatique",
           "adresse": "1 Avenue des Jeux, Paris",
           "ville": "Paris",
           "code_postal": "75001",
           "capacite": 15000
       }
   ]

Consultation des événements
---------------------------

**Endpoint :** ``GET /api/evenements/``

.. code-block:: json

   [
       {
           "id": 1,
           "description": "Finales de natation",
           "date": "2024-07-28",
           "horraire": "20:00:00",
           "nb_place_total": 15000,
           "nb_place_restante": 12500,
           "lieu": {
               "id": 1,
               "nom": "Centre Aquatique",
               "adresse": "1 Avenue des Jeux, Paris"
           },
           "epreuves": [
               {
                   "id": 1,
                   "libelle": "100m nage libre hommes",
                   "genre": "homme",
                   "tour": "finale",
                   "discipline": {
                       "id": 1,
                       "nom": "Natation",
                       "icone": "🏊‍♂️"
                   }
               }
           ]
       }
   ]

Création d'événements (Employés/Admins)
---------------------------------------

**Endpoint :** ``POST /api/evenements/``

.. code-block:: json

   {
       "description": "Demi-finales 200m dos",
       "lieu_id": 1,
       "date": "2024-07-29",
       "horraire": "19:30:00",
       "nb_place_total": 15000,
       "epreuve_ids": [2, 3]
   }

Gestion des épreuves
====================

Création d'épreuve (Employés/Admins)
------------------------------------

**Endpoint :** ``POST /api/epreuves/``

.. code-block:: json

   {
       "libelle": "200m papillon femmes",
       "genre": "femme",
       "tour": "finale",
       "discipline_id": 1,
       "evenement_id": 2
   }

**Validation automatique :** L'API vérifie qu'aucune épreuve avec le même libellé n'existe pour la discipline.

Consultation des épreuves par discipline
----------------------------------------

**Endpoint :** ``GET /api/epreuves/?discipline=1``

Filtrage et pagination
======================

Paramètres de filtrage disponibles
----------------------------------

**Événements :**

- ``?date=2024-07-28`` : Filtrer par date
- ``?lieu=1`` : Filtrer par lieu
- ``?page=2`` : Pagination

**Épreuves :**

- ``?discipline=1`` : Filtrer par discipline
- ``?genre=homme`` : Filtrer par genre
- ``?tour=finale`` : Filtrer par tour

Exemple avec curl
-----------------

.. code-block:: bash

   # Récupérer les événements du 28 juillet
   curl -H "Authorization: Bearer YOUR_TOKEN" \
        "http://127.0.0.1:8000/api/evenements/?date=2024-07-28"

Gestion des offres
==================

Consultation des offres
-----------------------

**Endpoint :** ``GET /api/offres/``

.. code-block:: json

   [
       {
           "id": 1,
           "nom": "Pack Solo",
           "prix": "75.00",
           "nombre_personnes": 1
       },
       {
           "id": 2,
           "nom": "Pack Famille",
           "prix": "250.00",
           "nombre_personnes": 4
       }
   ]

Création d'offre (Admins uniquement)
------------------------------------

**Endpoint :** ``POST /api/offres/``

.. code-block:: json

   {
       "nom": "Pack VIP",
       "prix": "500.00",
       "nombre_personnes": 2
   }

Gestion des utilisateurs (Admins)
=================================

Création d'employé
------------------

**Endpoint :** ``POST /auth/register/employee/``

.. code-block:: json

   {
       "email": "employe@jo2024.fr",
       "password": "MotDePasseSecurise123!",
       "nom": "Martin",
       "prenom": "Sophie",
       "matricule": "EMP001",
       "identifiant_telephone": "TEL001"
   }

Consultation des profils utilisateurs
-------------------------------------

**Endpoint :** ``GET /users/clients/`` (liste des clients)
**Endpoint :** ``GET /users/employees/`` (liste des employés)

Gestion des erreurs
===================

Codes de statut HTTP
--------------------

- **200 OK** : Requête réussie
- **201 Created** : Ressource créée avec succès
- **400 Bad Request** : Données invalides
- **401 Unauthorized** : Authentification requise
- **403 Forbidden** : Permissions insuffisantes
- **404 Not Found** : Ressource introuvable
- **500 Internal Server Error** : Erreur serveur

Exemples d'erreurs courantes
----------------------------

**Token expiré :**

.. code-block:: json

   {
       "detail": "Token is invalid or expired",
       "code": "token_not_valid"
   }

**Données manquantes :**

.. code-block:: json

   {
       "email": ["Ce champ est obligatoire."],
       "password": ["Ce champ est obligatoire."]
   }

**Permissions insuffisantes :**

.. code-block:: json

   {
       "detail": "Vous n'avez pas la permission d'effectuer cette action."
   }

Tests avec Postman
==================

Collection Postman recommandée
------------------------------

1. **Dossier Authentication**
   - POST /auth/register/client/
   - POST /auth/register/employee/
   - POST /auth/login/

2. **Dossier API Events**
   - GET /api/disciplines/
   - GET/POST /api/lieux/
   - GET/POST /api/evenements/
   - GET/POST /api/epreuves/
   - GET/POST /api/offres/

3. **Variables d'environnement**
   - ``base_url`` : http://127.0.0.1:8000
   - ``access_token`` : Votre token JWT

Exemples d'intégration frontend
===============================

JavaScript/Fetch
----------------

.. code-block:: javascript

   // Connexion
   const login = async (email, password) => {
       const response = await fetch('/auth/login/', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json',
           },
           body: JSON.stringify({ email, password })
       });

       const data = await response.json();
       localStorage.setItem('access_token', data.access);
       return data;
   };

   // Récupération des événements
   const getEvents = async () => {
       const token = localStorage.getItem('access_token');
       const response = await fetch('/api/evenements/', {
           headers: {
               'Authorization': `Bearer ${token}`,
               'Content-Type': 'application/json',
           }
       });

       return await response.json();
   };

Python/Requests
---------------

.. code-block:: python

   import requests

   # Connexion
   login_data = {
       'email': 'client@example.com',
       'password': 'MonMotDePasse123!'
   }

   response = requests.post(
       'http://127.0.0.1:8000/auth/login/',
       json=login_data
   )

   tokens = response.json()
   access_token = tokens['access']

   # Utilisation de l'API
   headers = {
       'Authorization': f'Bearer {access_token}',
       'Content-Type': 'application/json'
   }

   events = requests.get(
       'http://127.0.0.1:8000/api/evenements/',
       headers=headers
   ).json()

Bonnes pratiques
================

Sécurité
--------

- **Toujours utiliser HTTPS** en production
- **Renouveler les tokens JWT** régulièrement
- **Ne jamais exposer** les tokens dans les URLs
- **Valider les données** côté client ET serveur

Performance
-----------

- **Utiliser la pagination** pour les grandes listes
- **Mettre en cache** les données statiques (disciplines, lieux)
- **Limiter les requêtes** avec un système de throttling

Gestion des erreurs
-------------------

- **Toujours vérifier** le code de statut HTTP
- **Afficher des messages** d'erreur compréhensibles
- **Implémenter un système** de retry pour les erreurs temporaires

Ressources supplémentaires
==========================

- **Documentation API complète** : :doc:`api/index`
- **Authentification détaillée** : :doc:`authentication/index`
- **Gestion des utilisateurs** : :doc:`users/index`
- **Tests automatisés** : Consultez le dossier ``tests/``

Support et dépannage
====================

En cas de problème :

1. Vérifiez les logs Django
2. Testez avec des outils comme Postman
3. Consultez la documentation des modules spécifiques
4. Vérifiez la configuration dans :doc:`configuration`
