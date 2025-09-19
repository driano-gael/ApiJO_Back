Permissions
===========

.. automodule:: authentication.permissions
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Le module **permissions** définit les classes de permissions personnalisées basées sur les rôles utilisateurs.

Permissions disponibles
======================

IsAdmin
-------

**Usage :** Accès réservé aux administrateurs uniquement

- Vérifie que l'utilisateur est authentifié
- Vérifie que l'utilisateur a le rôle 'admin'
- Utilisée pour les opérations sensibles (création/modification/suppression)

.. code-block:: python

   permission_classes = [IsAuthenticated, IsAdmin]

IsAdminOrEmploye
---------------

**Usage :** Accès pour les administrateurs et employés

- Permet aux utilisateurs avec les rôles 'admin' ou 'employe'
- Exclut les clients des opérations nécessitant un statut professionnel
- Utilisée pour les fonctionnalités métier avancées

.. code-block:: python

   permission_classes = [IsAuthenticated, IsAdminOrEmploye]

IsAdminOrAuthenticatedReadOnly
-----------------------------

**Usage :** Admin complet, autres utilisateurs en lecture seule

- **Administrateurs** : Accès complet (GET, POST, PUT, DELETE)
- **Autres utilisateurs authentifiés** : Lecture seule (GET, HEAD, OPTIONS)
- **Utilisateurs non authentifiés** : Aucun accès

.. code-block:: python

   permission_classes = [IsAdminOrAuthenticatedReadOnly]

Architecture des permissions
===========================

**Hiérarchie des rôles :**

1. **Admin** : Accès complet à toutes les ressources
2. **Employé** : Accès aux fonctionnalités métier
3. **Client** : Accès limité aux ressources publiques

**Utilisation dans les vues :**

.. code-block:: python

   # Lecture publique, écriture admin
   class EvenementListView(ListAPIView):
       permission_classes = [AllowAny]  # Lecture

   class EvenementCreateView(CreateAPIView):
       permission_classes = [IsAuthenticated, IsAdmin]  # Écriture

Exemples d'utilisation
=====================

.. code-block:: python

   from authentication.permissions import IsAdmin, IsAdminOrEmploye

   # Vue réservée aux admins
   class AdminOnlyView(APIView):
       permission_classes = [IsAuthenticated, IsAdmin]

   # Vue pour le personnel (admin + employés)
   class StaffView(APIView):
       permission_classes = [IsAuthenticated, IsAdminOrEmploye]
