Sérialiseur Client
==================

.. automodule:: authentication.serializers.client
   :undoc-members:
   :members:
   :show-inheritance:

Description
-----------

Le **ClientRegisterSerializer** gère l'inscription des clients avec validation complète et création automatique du profil.

Fonctionnalités
---------------

Validation avancée
^^^^^^^^^^^^^^^^^^

- **Email** : Validation avec ``EmailValidator`` (anti-spam, unicité)
- **Mot de passe** : Validation avec ``StrongPasswordValidator`` (12 car. min, complexité)
- **Nom/Prénom** : Minimum 2 caractères chacun
- **Téléphone** : Minimum 10 chiffres, chiffres uniquement

Création automatique
^^^^^^^^^^^^^^^^^^^^

- Crée l'utilisateur de base avec le rôle ``'client'``
- Crée automatiquement le profil ``ClientProfile`` associé
- Génère une clé chiffrée pour le client

Champs du sérialiseur
---------------------

**Champs d'entrée (write_only) :**

- ``email`` : Adresse email (avec validation EmailValidator)
- ``password`` : Mot de passe sécurisé
- ``nom`` : Nom de famille (min 2 caractères)
- ``prenom`` : Prénom (min 2 caractères)
- ``telephone`` : Numéro de téléphone (min 10 chiffres)

Validations personnalisées
--------------------------

validate_email()
^^^^^^^^^^^^^^^^
Vérifie l'unicité de l'email dans la base de données.

.. automethod:: authentication.serializers.client.ClientRegisterSerializer.validate_email

validate_password()
^^^^^^^^^^^^^^^^^^^
Applique les règles du ``StrongPasswordValidator`` configuré dans settings.py.

.. automethod:: authentication.serializers.client.ClientRegisterSerializer.validate_password

validate_nom() / validate_prenom()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Contrôle que le nom/prénom fait au moins 2 caractères.

.. automethod:: authentication.serializers.client.ClientRegisterSerializer.validate_nom
.. automethod:: authentication.serializers.client.ClientRegisterSerializer.validate_prenom

validate_telephone()
^^^^^^^^^^^^^^^^^^^^
Vérifie que le téléphone contient uniquement des chiffres et fait au moins 10 caractères.

.. automethod:: authentication.serializers.client.ClientRegisterSerializer.validate_telephone

Processus de création
---------------------

1. **Validation** de tous les champs
2. **Création de l'utilisateur** avec ``User.objects.create_user()``
3. **Assignation du rôle** ``'client'``
4. **Création du profil** ``ClientProfile`` avec les données personnelles
5. **Génération automatique** de la clé chiffrée

