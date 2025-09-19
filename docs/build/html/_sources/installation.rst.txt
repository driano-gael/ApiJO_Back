Installation
============

Ce guide vous accompagne dans l'installation complète de l'API ApiJO.

Prérequis
---------

- Python 3.x
- PostgreSQL
- Un environnement virtuel Python (recommandé)
- Redis (optionnel, pour le cache)

Installation de l'environnement
-----------------------------

1. Cloner le dépôt
^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   git clone [url-du-repo]
   cd ApiJO_Back

2. Créer l'environnement virtuel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   python -m venv .venv
   .venv\Scripts\activate  # Sur Windows
   source .venv/bin/activate  # Sur Linux/Mac

3. Installer les dépendances
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   pip install -r requirements.txt

Configuration de la base de données
--------------------------------

1. Créer une base de données PostgreSQL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sql

   CREATE DATABASE apijoback;
   CREATE USER apijouser WITH PASSWORD 'votre_mot_de_passe';
   GRANT ALL PRIVILEGES ON DATABASE apijoback TO apijouser;

2. Configurer les variables d'environnement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Créez un fichier `.env` à la racine du projet :

.. code-block:: bash

   DB_NAME=apijoback
   DB_USER=apijouser
   DB_PASSWORD=votre_mot_de_passe
   DB_HOST=localhost
   DB_PORT=5432
   SECRET_KEY=votre_clé_secrète
   DEBUG=True

Configuration de Django
--------------------

1. Appliquer les migrations
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   python manage.py migrate

2. Créer un superutilisateur
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   python manage.py createsuperuser

3. Collecter les fichiers statiques
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   python manage.py collectstatic

Configuration du CORS
------------------

Modifier `settings.py` pour autoriser les origines de votre frontend :

.. code-block:: python

   CORS_ALLOWED_ORIGINS = [
       "http://localhost:3000",  # Frontend React
       "http://127.0.0.1:3000",
   ]

   CORS_ALLOW_CREDENTIALS = True

Installation de Redis (optionnel)
------------------------------

1. Installer Redis
^^^^^^^^^^^^^^^

- **Windows** : Télécharger et installer via https://github.com/microsoftarchive/redis/releases
- **Linux** : ``sudo apt-get install redis-server``
- **Mac** : ``brew install redis``

2. Configurer Redis dans settings.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   CACHES = {
       'default': {
           'BACKEND': 'django_redis.cache.RedisCache',
           'LOCATION': 'redis://127.0.0.1:6379/1',
           'OPTIONS': {
               'CLIENT_CLASS': 'django_redis.client.DefaultClient',
           }
       }
   }

Vérification de l'installation
---------------------------

1. Tests de base
^^^^^^^^^^^^^

.. code-block:: cmd

   python manage.py check
   python manage.py test

2. Lancer le serveur
^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   python manage.py runserver

L'API devrait être accessible à http://localhost:8000/

3. Vérifier l'interface d'administration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Accédez à http://localhost:8000/admin avec les identifiants du superutilisateur

Dépannage
--------

Problèmes courants :

- **Erreur de connexion à la base de données** : Vérifiez les paramètres dans `.env`
- **Erreur CORS** : Vérifiez CORS_ALLOWED_ORIGINS dans settings.py
- **Erreur de dépendances** : Réinstallez avec ``pip install -r requirements.txt``
- **Erreur de migrations** : Essayez ``python manage.py migrate --run-syncdb``

Prochaines étapes
---------------

1. Consultez le guide de :doc:`configuration` pour la configuration avancée
2. Explorez la documentation des :doc:`api/index` pour comprendre les endpoints
3. Testez l'authentification avec :doc:`authentication/index`
