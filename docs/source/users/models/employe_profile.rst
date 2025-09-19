Modèle EmployeProfile
====================

.. automodule:: users.models.employe
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Le modèle **EmployeProfile** étend les informations de base de l'utilisateur avec des données professionnelles spécifiques aux employés.

Fonctionnalités
===============

Données professionnelles
~~~~~~~~~~~~~~~~~~~~~~~~

- Nom et prénom de l'employé
- Matricule unique (identifiant professionnel)
- Identifiant téléphonique professionnel

Gestion du personnel
~~~~~~~~~~~~~~~~~~~

- Création contrôlée par les administrateurs
- Traçabilité des employés via matricule
- Identification professionnelle sécurisée

Relation OneToOne
~~~~~~~~~~~~~~~~

- Lié de manière unique à un utilisateur User
- Création par les administrateurs uniquement

Attributs du modèle
===================

.. py:attribute:: user
   :type: OneToOneField(User, related_name='employe_profile')

   Relation unique vers l'utilisateur de base

.. py:attribute:: nom
   :type: CharField(max_length=100)

   Nom de famille de l'employé

.. py:attribute:: prenom
   :type: CharField(max_length=100)

   Prénom de l'employé

.. py:attribute:: matricule
   :type: CharField(max_length=50, unique=True)

   Numéro de matricule unique de l'employé

.. py:attribute:: identifiant_telephone
   :type: CharField(max_length=255)

   Identifiant téléphonique professionnel (format libre)

Contraintes et validations
=========================

Matricule unique
~~~~~~~~~~~~~~~

- **Contrainte d'unicité** sur le matricule
- Empêche les doublons d'employés
- Facilite l'identification professionnelle

Représentation textuelle
~~~~~~~~~~~~~~~~~~~~~~~

La méthode ``__str__()`` retourne le nom complet avec matricule :

.. code-block:: python

   def __str__(self):
       return f"{self.nom} {self.prenom} ({self.matricule})"

Tri automatique
~~~~~~~~~~~~~~

Les profils employé sont triés par nom puis prénom par défaut.

Utilisation
===========

**Création par admin :**

.. code-block:: python

   # Lors de l'inscription employé (admin uniquement)
   user = User.objects.create_user(
       email='employe@jeux-olympiques.fr',
       password='password',
       role='employe'
   )

   # Création du profil professionnel
   EmployeProfile.objects.create(
       user=user,
       nom='Martin',
       prenom='Sophie',
       matricule='EMP001',
       identifiant_telephone='TEL-JO-2024-001'
   )

**Accès aux données :**

.. code-block:: python

   # Via l'utilisateur
   user = User.objects.get(email='employe@jeux-olympiques.fr')
   profile = user.employe_profile

   print(f"Employé: {profile}")  # "Martin Sophie (EMP001)"
   print(f"Matricule: {profile.matricule}")
   print(f"Tel pro: {profile.identifiant_telephone}")

**Recherche par matricule :**

.. code-block:: python

   # Trouver un employé par matricule
   employe = EmployeProfile.objects.get(matricule='EMP001')
   print(f"Email pro: {employe.user.email}")
   print(f"Statut: {employe.user.is_active}")

Gestion professionnelle
======================

**Identification d'équipe :**

.. code-block:: python

   # Lister tous les employés actifs
   employes_actifs = EmployeProfile.objects.filter(
       user__is_active=True,
       user__role='employe'
   ).order_by('nom', 'prenom')

   for employe in employes_actifs:
       print(f"{employe.matricule}: {employe}")

**Contrôle d'accès :**

.. code-block:: python

   # Vérifier les droits d'un employé
   def check_employe_access(matricule, zone):
       try:
           employe = EmployeProfile.objects.get(matricule=matricule)
           if employe.user.is_active:
               return authorize_zone_access(employe, zone)
       except EmployeProfile.DoesNotExist:
           return False

Différences avec ClientProfile
=============================

**Champs spécifiques :**
- ``matricule`` (unique) au lieu de ``telephone``
- ``identifiant_telephone`` professionnel (format libre)
- Pas de ``cle_chiffree`` (sécurité différente)

**Usage :**
- Création par admin vs inscription libre
- Identification professionnelle vs personnelle
- Gestion du personnel vs gestion client
