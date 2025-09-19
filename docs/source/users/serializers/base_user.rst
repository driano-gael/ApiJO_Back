Sérialiseur User (Base)
======================

.. automodule:: users.serializers.base_user
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Le **UserSerializer** gère la sérialisation du modèle User personnalisé avec gestion sécurisée des mots de passe.

Fonctionnalités
===============

Gestion sécurisée des mots de passe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Écriture seule** : Le mot de passe n'apparaît jamais dans les réponses JSON
- **Hachage automatique** : Utilise `set_password()` pour le hachage sécurisé
- **Validation** : Applique les règles de validation Django

Champs du sérialiseur
====================

.. py:attribute:: id
   :type: IntegerField (read-only)

   Identifiant unique de l'utilisateur

.. py:attribute:: email
   :type: EmailField

   Adresse email unique servant d'identifiant

.. py:attribute:: password
   :type: CharField (write-only)

   Mot de passe en clair pour création/mise à jour (jamais exposé en lecture)

.. py:attribute:: role
   :type: CharField

   Rôle de l'utilisateur (client, employe, admin)

.. py:attribute:: is_active
   :type: BooleanField

   Statut actif de l'utilisateur

Méthodes personnalisées
======================

create()
~~~~~~~~

Crée un nouvel utilisateur avec hachage sécurisé du mot de passe.

update()
~~~~~~~~

Met à jour un utilisateur existant, avec gestion spéciale du mot de passe si fourni.

Exemple d'utilisation
====================

.. code-block:: python

   # Sérialisation d'un utilisateur (sans mot de passe)
   user = User.objects.get(email='user@example.com')
   serializer = UserSerializer(user)
   data = serializer.data

   # Création via sérialiseur
   serializer = UserSerializer(data={
       'email': 'newuser@example.com',
       'password': 'motdepassesecurise123',
       'role': 'client'
   })
   if serializer.is_valid():
       user = serializer.save()  # Le mot de passe sera haché automatiquement

Sécurité
========

- **Pas de fuite de mot de passe** : Le champ password est write-only
- **Hachage automatique** : Utilisation de la méthode Django `set_password()`
- **Validation** : Respect des règles de sécurité configurées
