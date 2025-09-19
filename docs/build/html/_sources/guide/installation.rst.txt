Installation
============

Ce guide vous accompagne dans l'installation complète de l'API ApiJO.

# Prérequis

- Python 3.x
- PostgreSQL
- Un environnement virtuel Python (recommandé)
- Redis (optionnel, pour le cache)

Installation de l'environnement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Cloner le dépôt
^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   git clone [url-du-repo]
   cd ApiJO_Back

2. Créer l'environnement virtuel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   python -m venv .venv
   .venv\Scripts\activate  # Sur Windows
   source .venv/bin/activate  # Sur Linux/Mac

3. Installer les dépendances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   pip install -r requirements.txt

Configuration de la base de données
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Créer une base de données PostgreSQL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sql

   CREATE DATABASE apijoback;
   CREATE USER apijouser WITH PASSWORD 'votre_mot_de_passe';
   GRANT ALL PRIVILEGES ON DATABASE apijoback TO apijouser;

2. Configurer les variables d'environnement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copier le fichier `.env.exemple` et le renommer en `.env` à la racine du projet, puis modifier les valeurs :

.. code-block:: bash

    # Configuration Django
    DEBUG=True
    SECRET_KEY='your-secret-key'
    ALLOWED_HOSTS=127.0.0.1,localhost

    # Configuration Base de données
    DATABASE_NAME=your_database_name
    DATABASE_USER=your_database_user
    DATABASE_PASSWORD=your_database_password
    DATABASE_HOST=localhost
    DATABASE_PORT=5432

    # Configuration CORS
    CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

    # Configuration JWT
    ACCESS_TOKEN_LIFETIME=00:00:30
    REFRESH_TOKEN_LIFETIME=08:00:00

    # Configuration Admin par défaut
    ADMIN_EMAIL=admin@example.com
    ADMIN_PASSWORD=your_admin_password
    ADMIN_NOM=Admin
    ADMIN_PRENOM=admin
    ADMIN_MATRICULE=ADM001

Configuration de Django
~~~~~~~~~~~~~~~~~~~~~~~

1. Appliquer les migrations
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   python manage.py migrate

2. Créer un administrateur
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   python manage.py createAdmin

3. Collecter les fichiers statiques
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   python manage.py collectstatic

4. Peupler la base de données avec des données initiales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   python manage.py populate_jo_2


Vérification de l'installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Tests de base
^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   python manage.py check
   python manage.py test

2. Lancer le serveur
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cmd

   python manage.py runserver

L'API devrait être accessible à http://localhost:8000/

3. Vérifier l'acces aux endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Accédez à http://localhost:8000/api/evenement/

Dépannage
~~~~~~~~~

Problèmes courants :

- **Erreur de connexion à la base de données** : Vérifiez les paramètres dans `.env`
- **Erreur CORS** : Vérifiez CORS_ALLOWED_ORIGINS dans settings.py
- **Erreur de dépendances** : Réinstallez avec ``pip install -r requirements.txt``
- **Erreur de migrations** : Essayez ``python manage.py migrate --run-syncdb``
