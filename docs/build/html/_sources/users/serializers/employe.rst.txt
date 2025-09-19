Sérialiseur Employé
===================

.. automodule:: users.serializers.employe
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Le **EmployeProfileSerializer** gère la sérialisation du modèle EmployeProfile avec les données professionnelles des employés.

Fonctionnalités
===============

Données professionnelles
~~~~~~~~~~~~~~~~~~~~~~~~

- Nom, prénom et matricule de l'employé
- Identifiant téléphonique professionnel
- Relation avec l'utilisateur de base

Gestion du personnel
~~~~~~~~~~~~~~~~~~~

- **Matricule unique** pour identification professionnelle
- **Données de contact** professionnel
- **Traçabilité** des employés

Champs du sérialiseur
====================

.. py:attribute:: user
   :type: UserSerializer (nested, read-only)

   Informations de l'utilisateur associé (email, rôle employe)

.. py:attribute:: nom
   :type: CharField

   Nom de famille de l'employé

.. py:attribute:: prenom
   :type: CharField

   Prénom de l'employé

.. py:attribute:: matricule
   :type: CharField

   Numéro de matricule unique (identifiant professionnel)

.. py:attribute:: identifiant_telephone
   :type: CharField

   Identifiant téléphonique professionnel

Relations optimisées
===================

Inclut automatiquement les informations utilisateur pour un accès complet aux données d'employé.

Exemple d'utilisation
====================

.. code-block:: python

   # Sérialisation d'un profil employé complet
   employe_profile = EmployeProfile.objects.get(matricule='EMP001')
   serializer = EmployeProfileSerializer(employe_profile)
   data = serializer.data

   # Résultat avec données utilisateur et professionnel
   {
     'id': 1,
     'user': {
       'id': 3,
       'email': 'martin@jeux-olympiques.fr',
       'role': 'employe',
       'is_active': True
     },
     'nom': 'Martin',
     'prenom': 'Sophie',
     'matricule': 'EMP001',
     'identifiant_telephone': 'TEL-JO-2024-001'
   }

Usage professionnel
==================

Ce sérialiseur est utilisé pour :
- **Gestion du personnel** par les administrateurs
- **Annuaires internes** d'employés
- **Systèmes de badges** et contrôle d'accès
- **Interfaces de gestion RH**
