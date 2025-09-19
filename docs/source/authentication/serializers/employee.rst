Sérialiseur Employee
====================

.. automodule:: authentication.serializers.employee
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Le **EmployeeRegisterSerializer** gère l'inscription des employés par les administrateurs avec validation complète.

Fonctionnalités
---------------

Création réservée aux admins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Seuls les administrateurs peuvent créer des comptes employé
- Processus d'inscription contrôlé pour le personnel

Validation complète
^^^^^^^^^^^^^^^^^^^

- **Email** : Validation d'unicité
- **Mot de passe** : Validation avec ``StrongPasswordValidator``
- **Données professionnelles** : matricule et identifiant téléphonique

Création automatique
^^^^^^^^^^^^^^^^^^^^

- Crée l'utilisateur de base avec le rôle ``'employe'``
- Crée automatiquement le profil ``EmployeProfile`` associé
- Gestion des données professionnelles spécifiques

Champs du sérialiseur
---------------------

**Champs d'entrée (write_only) :**

- ``email`` : Adresse email professionnelle
- ``password`` : Mot de passe sécurisé
- ``nom`` : Nom de famille de l'employé
- ``prenom`` : Prénom de l'employé
- ``matricule`` : Numéro de matricule unique
- ``identifiant_telephone`` : Identifiant téléphonique professionnel

Validations
-----------

validate_email()
^^^^^^^^^^^^^^^^
Vérifie que l'email n'est pas déjà utilisé par un autre utilisateur.

Validation du mot de passe
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Utilise le système de validation Django avec ``StrongPasswordValidator`` pour imposer les règles de sécurité.

Processus de création
---------------------

1. **Extraction des données** personnelles et professionnelles
2. **Validation du mot de passe** selon les règles Django
3. **Création de l'utilisateur** avec le rôle ``'employe'``
4. **Création du profil employé** avec matricule et identifiant téléphonique
5. **Retour du profil** EmployeProfile créé

Exemple d'utilisation
---------------------

.. code-block:: python

   # Création d'un employé par un administrateur
   data = {
       'email': 'employe@jo2024.fr',
       'password': 'MotDePasseSecurise123!',
       'nom': 'Martin',
       'prenom': 'Sophie',
       'matricule': 'EMP001',
       'identifiant_telephone': 'TEL001'
   }

   serializer = EmployeeRegisterSerializer(data=data)
   if serializer.is_valid():
       employe_profile = serializer.save()
       # L'utilisateur et son profil employé sont créés automatiquement

Différences avec ClientRegisterSerializer
=========================================

- **Pas de validation téléphone** (format libre pour usage professionnel)
- **Champs spécifiques** : matricule et identifiant téléphonique
- **Rôle différent** : ``'employe'`` au lieu de ``'client'``
- **Retour différent** : retourne le EmployeProfile au lieu du User
