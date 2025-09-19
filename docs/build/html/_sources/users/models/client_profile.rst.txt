Modèle ClientProfile
===================

.. automodule:: users.models.client
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Le modèle **ClientProfile** étend les informations de base de l'utilisateur avec des données spécifiques aux clients et une sécurité renforcée.

Fonctionnalités
===============

Données personnelles
~~~~~~~~~~~~~~~~~~~~

- Nom et prénom complets
- Numéro de téléphone personnel
- Informations de contact client

Sécurité automatique
~~~~~~~~~~~~~~~~~~~~

- **Clé chiffrée** générée automatiquement
- Basée sur l'email et le nom (SHA256)
- Protection des données personnelles

Relation OneToOne
~~~~~~~~~~~~~~~~~

- Lié de manière unique à un utilisateur User
- Création automatique lors de l'inscription client

Attributs du modèle
===================

.. py:attribute:: user
   :type: OneToOneField(User, related_name='client_profile')

   Relation unique vers l'utilisateur de base

.. py:attribute:: nom
   :type: CharField(max_length=100)

   Nom de famille du client

.. py:attribute:: prenom
   :type: CharField(max_length=100)

   Prénom du client

.. py:attribute:: telephone
   :type: CharField(max_length=20)

   Numéro de téléphone personnel

.. py:attribute:: cle_chiffree
   :type: CharField(max_length=255)

   Clé de sécurité générée automatiquement (SHA256)

Fonctionnalités automatiques
============================

Génération de clé chiffrée
~~~~~~~~~~~~~~~~~~~~~~~~~~

La méthode ``save()`` génère automatiquement une clé chiffrée unique :

.. code-block:: python

   def save(self, *args, **kwargs):
       if not self.cle_chiffree:
           raw_key = f"{self.user.email}-{self.nom}"
           self.cle_chiffree = hashlib.sha256(raw_key.encode('utf-8')).hexdigest()
       super().save(*args, **kwargs)

**Processus :**
1. Combine email + nom
2. Génère un hash SHA256
3. Stocke la clé de manière sécurisée

Tri automatique
~~~~~~~~~~~~~~

Les profils client sont triés par nom puis prénom par défaut.

Utilisation
===========

**Création automatique :**

.. code-block:: python

   # Lors de l'inscription client
   user = User.objects.create_user(
       email='client@example.com',
       password='password',
       role='client'
   )

   # Création du profil associé
   ClientProfile.objects.create(
       user=user,
       nom='Dupont',
       prenom='Jean',
       telephone='0123456789'
   )
   # La clé chiffrée sera générée automatiquement

**Accès aux données :**

.. code-block:: python

   # Via l'utilisateur
   user = User.objects.get(email='client@example.com')
   profile = user.client_profile

   print(f"Client: {profile.nom} {profile.prenom}")
   print(f"Téléphone: {profile.telephone}")
   print(f"Clé: {profile.cle_chiffree}")

**Depuis le profil :**

.. code-block:: python

   # Accès aux informations utilisateur
   profile = ClientProfile.objects.get(nom='Dupont')
   print(f"Email: {profile.user.email}")
   print(f"Rôle: {profile.user.role}")

Sécurité et confidentialité
===========================

**Protection des données :**
- Clé chiffrée unique pour chaque client
- Hash irréversible (SHA256)
- Pas de stockage de données sensibles en clair

**Traçabilité :**
- Lien permanent avec l'utilisateur
- Historique via les relations Django
- Possibilité d'audit des accès

Exemples d'usage métier
======================

**Gestion des réservations :**

.. code-block:: python

   # Identifier un client pour une réservation
   client = ClientProfile.objects.get(cle_chiffree=cle_recue)

   # Créer une réservation pour ce client
   reservation = Reservation.objects.create(
       client=client,
       evenement=evenement,
       nb_places=2
   )

**Génération de QR codes :**

.. code-block:: python

   # Utiliser la clé chiffrée pour les billets
   qr_data = f"CLIENT:{client.cle_chiffree}:EVENT:{evenement.id}"
   generate_qr_code(qr_data)
