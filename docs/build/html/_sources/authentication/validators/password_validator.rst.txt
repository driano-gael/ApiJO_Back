Validateur de Mot de Passe
===========================

.. automodule:: authentication.validators.passwordValidator
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Le **StrongPasswordValidator** impose des règles strictes de sécurité pour les mots de passe utilisateur.

Règles de sécurité
==================

Longueur minimale
~~~~~~~~~~~~~~~~~

- **12 caractères minimum** requis
- Augmente significativement la résistance aux attaques par force brute

Complexité obligatoire
~~~~~~~~~~~~~~~~~~~~~

Le mot de passe doit contenir **au moins un caractère** de chaque type :

- **Majuscule** : A-Z
- **Minuscule** : a-z
- **Chiffre** : 0-9
- **Caractère spécial** : Tout caractère non alphanumérique (!@#$%^&* etc.)

Configuration Django
====================

Ajout dans ``settings.py`` :

.. code-block:: python

   AUTH_PASSWORD_VALIDATORS = [
       {
           'NAME': 'authentication.validators.passwordValidator.StrongPasswordValidator',
       },
   ]

Utilisation automatique
======================

Le validateur est utilisé automatiquement par :

- ``django.contrib.auth.password_validation.validate_password()``
- Les sérialiseurs d'inscription (``ClientRegisterSerializer``, ``EmployeeRegisterSerializer``)
- Les formulaires d'administration Django

Messages d'erreur
=================

- **Longueur insuffisante** : "Le mot de passe doit contenir au moins 12 caractères."
- **Manque majuscule** : "Le mot de passe doit contenir au moins une majuscule."
- **Manque minuscule** : "Le mot de passe doit contenir au moins une minuscule."
- **Manque chiffre** : "Le mot de passe doit contenir au moins un chiffre."
- **Manque caractère spécial** : "Le mot de passe doit contenir au moins un caractère spécial."

Texte d'aide
============

"Le mot de passe doit contenir au moins 12 caractères, avec une majuscule, une minuscule, un chiffre et un caractère spécial."

Exemples
========

.. code-block:: python

   # ✅ Mots de passe valides
   "MonMotDePasse123!"
   "Secure_P@ssw0rd_2024"
   "MyStr0ng#Password"

   # ❌ Mots de passe invalides
   "password123"        # Pas de majuscule ni caractère spécial
   "PASSWORD123!"       # Pas de minuscule
   "MonMotDePasse!"     # Pas de chiffre
   "Short1!"           # Trop court (moins de 12 caractères)
