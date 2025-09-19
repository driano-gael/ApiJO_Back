Validateur Email
================

.. automodule:: authentication.validators.emailValidator
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Le **EmailValidator** offre une validation d'email avancée avec protection anti-spam intégrée.

Fonctionnalités
===============

Validation du format
~~~~~~~~~~~~~~~~~~~~

- Contrôle de la syntaxe avec regex avancée
- Vérification de la structure email standard

Protection anti-spam
~~~~~~~~~~~~~~~~~~~~

Liste des domaines interdits par défaut :
- ``tempmail.com``
- ``mailinator.com``
- ``yopmail.com``
- ``10minutemail.com``

Contrôle d'unicité
~~~~~~~~~~~~~~~~~~

- Vérification automatique que l'email n'est pas déjà enregistré
- Comparaison insensible à la casse

Configuration
=============

.. code-block:: python

   # Utilisation avec domaines par défaut
   validator = EmailValidator()

   # Configuration personnalisée
   validator = EmailValidator(forbidden_domains=[
       'exemple-spam.com',
       'email-jetable.fr'
   ])

Utilisation dans les sérialiseurs
=================================

.. code-block:: python

   from authentication.validators.emailValidator import EmailValidator

   class ClientRegisterSerializer(serializers.ModelSerializer):
       email = serializers.EmailField(
           write_only=True,
           validators=[EmailValidator()]
       )

Messages d'erreur
=================

- **Format invalide** : "Adresse e-mail invalide."
- **Domaine interdit** : "Les adresses e-mail jetables ne sont pas autorisées."
- **Email existant** : "Un utilisateur avec cet e-mail existe déjà."

Texte d'aide
============

"Utilisez une adresse e-mail valide, non temporaire, et qui n'est pas déjà enregistrée."
