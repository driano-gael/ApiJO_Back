Sérialiseur Admin
=================

.. automodule:: users.serializers.admin
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Le sérialiseur **Admin** gère la sérialisation pour les opérations administratives sur les utilisateurs et profils.

Fonctionnalités
===============

Gestion administrative
~~~~~~~~~~~~~~~~~~~~~

- **Opérations privilégiées** réservées aux administrateurs
- **Accès complet** aux données utilisateurs
- **Gestion des rôles** et permissions
- **Opérations de maintenance** des comptes

Sécurité administrative
~~~~~~~~~~~~~~~~~~~~~~

- **Contrôle d'accès strict** aux fonctions admin
- **Audit des modifications** importantes
- **Gestion des utilisateurs** par les administrateurs

Champs étendus
==============

Ce sérialiseur peut inclure des champs supplémentaires non disponibles aux utilisateurs standard :

- **Données sensibles** pour la gestion administrative
- **Métadonnées système** des comptes utilisateur
- **Historique des modifications** si applicable

Usage administratif
==================

Ce sérialiseur est utilisé pour :
- **Interface d'administration** des utilisateurs
- **Opérations de masse** sur les comptes
- **Gestion des rôles** et permissions
- **Maintenance du système** utilisateur

Exemple d'utilisation
====================

.. code-block:: python

   # Utilisé dans les vues administratives
   # Accès réservé aux utilisateurs avec rôle 'admin'

   users = User.objects.all()
   serializer = AdminUserSerializer(users, many=True)
   admin_data = serializer.data

   # Inclut des informations étendues pour l'administration

Sécurité
========

- **Accès restreint** : Seuls les administrateurs peuvent utiliser ce sérialiseur
- **Validation stricte** : Contrôles supplémentaires pour les opérations sensibles
- **Audit** : Traçabilité des modifications administratives
