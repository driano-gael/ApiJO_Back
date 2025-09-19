Vues d'Authentification
======================

Les vues gèrent l'inscription des utilisateurs et l'authentification JWT avec gestion des rôles.

Endpoints disponibles
====================

- **Inscription client** : Libre accès pour les nouveaux utilisateurs
- **Inscription employé** : Réservée aux administrateurs
- **Connexion JWT** : Authentification avec tokens enrichis
- **Rafraîchissement** : Renouvellement des tokens

Architecture des permissions
===========================

- **Inscription client** : ``AllowAny`` (accès libre)
- **Inscription employé** : ``IsAdminUser`` (admin uniquement)
- **Authentification** : ``AllowAny`` (accès libre)

.. toctree::
   :maxdepth: 2
   :caption: Vues disponibles

   client
   employee
   token
