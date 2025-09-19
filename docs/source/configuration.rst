Configuration
=============

Ce guide détaille la configuration de l'API ApiJO après installation.

Configuration Django
====================

Fichier settings.py
-------------------

Les principaux paramètres à configurer dans `ApiJO_Back/settings.py` :

Base de données
^^^^^^^^^^^^^^^

.. code-block:: python

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': os.environ.get('DB_NAME', 'apijoback'),
           'USER': os.environ.get('DB_USER', 'apijouser'),
           'PASSWORD': os.environ.get('DB_PASSWORD'),
           'HOST': os.environ.get('DB_HOST', 'localhost'),
           'PORT': os.environ.get('DB_PORT', '5432'),
       }
   }

Authentification JWT
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from datetime import timedelta

   SIMPLE_JWT = {
       'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
       'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
       'ROTATE_REFRESH_TOKENS': True,
       'BLACKLIST_AFTER_ROTATION': True,
   }

CORS (Cross-Origin Resource Sharing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   CORS_ALLOWED_ORIGINS = [
       "http://localhost:3000",  # Frontend React
       "http://127.0.0.1:3000",
   ]

   CORS_ALLOW_CREDENTIALS = True

Configuration des modèles
=========================

Paramètres par défaut des modèles
---------------------------------

Événements
^^^^^^^^^^

Les événements ont des paramètres par défaut configurables :

- **Nombre de places par défaut** : 1000 places
- **Gestion automatique** des places restantes

Configuration des rôles utilisateurs
====================================

L'API supporte trois rôles principaux :

Rôle Client
-----------

- **Permissions** : Consultation des événements et offres
- **Restrictions** : Pas d'accès admin
- **Profil** : ClientProfile avec informations personnelles

Rôle Employé
------------

- **Permissions** : Gestion des événements et épreuves
- **Restrictions** : Pas de création d'utilisateurs
- **Profil** : EmployeProfile avec matricule

Rôle Admin
----------

- **Permissions** : Accès complet à l'API
- **Capacités** : Création d'employés, gestion complète
- **Accès** : Django Admin + API complète

Configuration des validateurs
=============================

Validation des mots de passe
----------------------------

Configuration du `StrongPasswordValidator` :

.. code-block:: python

   AUTH_PASSWORD_VALIDATORS = [
       {
           'NAME': 'authentication.validators.StrongPasswordValidator',
           'OPTIONS': {
               'min_length': 12,
               'require_uppercase': True,
               'require_lowercase': True,
               'require_digits': True,
               'require_special': True,
           }
       },
   ]

Validation des emails
---------------------

Utilise le `EmailValidator` intégré avec vérifications anti-spam.

Configuration de l'API REST
===========================

Pagination
----------

.. code-block:: python

   REST_FRAMEWORK = {
       'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
       'PAGE_SIZE': 20
   }

Permissions par défaut
----------------------

.. code-block:: python

   REST_FRAMEWORK = {
       'DEFAULT_PERMISSION_CLASSES': [
           'rest_framework.permissions.IsAuthenticated',
       ],
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ],
   }

Configuration des médias
========================

Gestion des fichiers uploadés
-----------------------------

.. code-block:: python

   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

   # Taille maximale des fichiers (5MB)
   FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880

Configuration de production
===========================

Variables d'environnement essentielles
--------------------------------------

.. code-block:: bash

   # Sécurité
   DEBUG=False
   SECRET_KEY=votre_clé_très_sécurisée
   ALLOWED_HOSTS=votredomaine.com,www.votredomaine.com

   # Base de données production
   DB_NAME=apijoback_prod
   DB_HOST=votre_serveur_db
   DB_PASSWORD=mot_de_passe_très_sécurisé

   # HTTPS
   SECURE_SSL_REDIRECT=True
   SECURE_PROXY_SSL_HEADER=HTTP_X_FORWARDED_PROTO,https

Collecte des fichiers statiques
-------------------------------

.. code-block:: bash

   python manage.py collectstatic --noinput

Configuration logging
---------------------

.. code-block:: python

   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'handlers': {
           'file': {
               'level': 'INFO',
               'class': 'logging.FileHandler',
               'filename': 'django.log',
           },
       },
       'loggers': {
           'django': {
               'handlers': ['file'],
               'level': 'INFO',
               'propagate': True,
           },
       },
   }

Configuration personnalisée
===========================

Ajout de nouvelles disciplines
------------------------------

Les disciplines peuvent être ajoutées via :

1. **Django Admin** : Interface web
2. **API REST** : Endpoints dédiés
3. **Fixtures** : Chargement en lot

.. code-block:: python

   # Exemple de fixture pour disciplines
   [
       {
           "model": "api.discipline",
           "fields": {
               "nom": "Natation",
               "icone": "🏊‍♂️"
           }
       }
   ]

Configuration des permissions personnalisées
--------------------------------------------

Création de permissions spécifiques :

.. code-block:: python

   from rest_framework.permissions import BasePermission

   class IsEmployeeOrAdmin(BasePermission):
       def has_permission(self, request, view):
           return request.user.role in ['employe', 'admin']

Tests de configuration
======================

Vérification de la configuration
--------------------------------

.. code-block:: bash

   # Test des paramètres Django
   python manage.py check

   # Test de la base de données
   python manage.py dbshell

   # Test des migrations
   python manage.py showmigrations

   # Test de l'API
   python manage.py test

Configuration avancée
=====================

Cache Redis (optionnel)
-----------------------

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

Monitoring (optionnel)
----------------------

Configuration pour le monitoring avec des outils comme Sentry :

.. code-block:: python

   import sentry_sdk
   from sentry_sdk.integrations.django import DjangoIntegration

   sentry_sdk.init(
       dsn="votre_dsn_sentry",
       integrations=[DjangoIntegration()],
       traces_sample_rate=1.0,
   )

Dépannage
=========

Problèmes de configuration courants
-----------------------------------

**Erreur 500** : Vérifiez DEBUG=True en développement
**CORS** : Ajoutez votre frontend aux CORS_ALLOWED_ORIGINS
**JWT** : Vérifiez que les tokens ne sont pas expirés
**Permissions** : Contrôlez les rôles utilisateurs

Prochaines étapes
=================

Après la configuration :

1. Consultez le guide :doc:`utilisation` pour utiliser l'API
2. Explorez la documentation des :doc:`api/index` pour comprendre les endpoints
3. Testez l'authentification avec :doc:`authentication/index`
