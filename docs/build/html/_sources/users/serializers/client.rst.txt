Sérialiseur Client
==================

.. automodule:: users.serializers.client
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Le **ClientProfileSerializer** gère la sérialisation du modèle ClientProfile avec les données personnelles des clients.

Fonctionnalités
===============

Données personnelles complètes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Nom, prénom et coordonnées du client
- Relation avec l'utilisateur de base
- Accès aux informations de compte

Sécurité des données
~~~~~~~~~~~~~~~~~~~

- **Clé chiffrée** incluse de manière sécurisée
- **Données personnelles** protégées selon les bonnes pratiques
- **Relations** avec l'utilisateur optimisées

Champs du sérialiseur
====================

.. py:attribute:: user
   :type: UserSerializer (nested, read-only)

   Informations de l'utilisateur associé (email, rôle, etc.)

.. py:attribute:: nom
   :type: CharField

   Nom de famille du client

.. py:attribute:: prenom
   :type: CharField

   Prénom du client

.. py:attribute:: telephone
   :type: CharField

   Numéro de téléphone personnel

.. py:attribute:: cle_chiffree
   :type: CharField (read-only)

   Clé de sécurité générée automatiquement (SHA256)

Relations optimisées
===================

Le sérialiseur inclut automatiquement les informations de l'utilisateur associé pour éviter les requêtes supplémentaires à la base de données.

Exemple d'utilisation
====================

.. code-block:: python

   # Sérialisation d'un profil client complet
   client_profile = ClientProfile.objects.get(nom='Dupont')
   serializer = ClientProfileSerializer(client_profile)
   data = serializer.data

   # Résultat inclut les données utilisateur et profil
   {
     'id': 1,
     'user': {
       'id': 2,
       'email': 'dupont@example.com',
       'role': 'client',
       'is_active': True
     },
     'nom': 'Dupont',
     'prenom': 'Jean',
     'telephone': '0123456789',
     'cle_chiffree': 'abc123...hash256'
   }

Usage dans les vues
==================

Ce sérialiseur est utilisé pour :
- **Affichage des profils clients** dans l'interface admin
- **API de consultation** des informations client
- **Gestion des données personnelles** avec sécurité
