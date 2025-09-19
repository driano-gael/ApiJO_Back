Vues d'Authentification
=======================

Les vues gèrent l'inscription des utilisateurs et l'authentification JWT avec gestion des rôles.

# Architecture des permissions
- **Inscription client** : ``AllowAny`` (accès libre)
- **Inscription employé** : ``IsAdminUser`` (admin uniquement)
- **Authentification** : ``AllowAny`` (accès libre)

.. toctree::
   :maxdepth: 2
   :caption: Vues disponibles

   client
   employee
   token
