Modèle User (Base)
==================

.. automodule:: users.models.base_user
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Le modèle **User** remplace le modèle utilisateur Django standard en utilisant l'email comme identifiant unique et en ajoutant un système de rôles.

Caractéristiques principales
===========================

Email comme identifiant
~~~~~~~~~~~~~~~~~~~~~~~

- **USERNAME_FIELD** = 'email' (au lieu de 'username')
- Email unique et obligatoire pour chaque utilisateur
- Pas de champ username nécessaire

Système de rôles intégré
~~~~~~~~~~~~~~~~~~~~~~~

**Rôles disponibles :**
- ``'client'`` : Utilisateurs finaux (clients des JO)
- ``'employe'`` : Personnel autorisé
- ``'admin'`` : Administrateurs avec accès complet

Attributs du modèle
===================

.. py:attribute:: email
   :type: EmailField(unique=True)

   Adresse email unique servant d'identifiant de connexion

.. py:attribute:: role
   :type: CharField(max_length=10, choices=ROLE_CHOICES)

   Rôle de l'utilisateur dans le système (client/employe/admin)

.. py:attribute:: is_active
   :type: BooleanField(default=True)

   Statut actif de l'utilisateur (permet de désactiver sans supprimer)

.. py:attribute:: is_staff
   :type: BooleanField(default=False)

   Accès à l'interface d'administration Django

Méthodes personnalisées
======================

has_admin_access()
~~~~~~~~~~~~~~~~~

Vérifie si l'utilisateur a des privilèges d'administrateur.

.. code-block:: python

   if user.has_admin_access():
       # Autoriser l'accès aux fonctions admin
       pass

**Returns :** ``True`` si l'utilisateur est staff ou a le rôle 'admin'

Configuration Django
===================

**Dans settings.py :**

.. code-block:: python

   # Utilisation du modèle User personnalisé
   AUTH_USER_MODEL = 'users.User'

**Gestionnaire personnalisé :**

.. code-block:: python

   # Utilise UserManager pour les méthodes de création
   objects = UserManager()

Exemples d'utilisation
=====================

**Création d'utilisateurs :**

.. code-block:: python

   # Client
   client = User.objects.create_user(
       email='client@example.com',
       password='password123',
       role='client'
   )

   # Employé
   employe = User.objects.create_user(
       email='employe@jeux-olympiques.fr',
       password='password123',
       role='employe'
   )

   # Admin
   admin = User.objects.create_admin(
       email='admin@jeux-olympiques.fr',
       password='adminpassword'
   )

**Vérification des permissions :**

.. code-block:: python

   # Dans une vue ou une permission personnalisée
   if user.role == 'admin':
       # Accès administrateur
   elif user.role == 'employe':
       # Accès employé
   elif user.role == 'client':
       # Accès client standard

Relations avec les profils
=========================

- **ClientProfile** : Relation OneToOne via ``client_profile``
- **EmployeProfile** : Relation OneToOne via ``employe_profile``

.. code-block:: python

   # Accéder au profil client
   if user.role == 'client':
       client_profile = user.client_profile
       print(f"Nom: {client_profile.nom} {client_profile.prenom}")

   # Accéder au profil employé
   if user.role == 'employe':
       employe_profile = user.employe_profile
       print(f"Matricule: {employe_profile.matricule}")

Avantages du modèle personnalisé
===============================

- **Simplicité** : Un seul identifiant (email) au lieu de username + email
- **Sécurité** : Email unique difficile à deviner
- **Flexibilité** : Système de rôles intégré
- **Extensibilité** : Base solide pour les profils spécialisés
