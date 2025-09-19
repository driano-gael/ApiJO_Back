Module API - Gestion des Entités des Jeux Olympiques
=====================================================

Le module API gère toutes les entités principales des Jeux Olympiques :

- **Disciplines** : Sports olympiques avec leurs icônes
- **Lieux** : Sites sportifs où se déroulent les événements
- **Événements** : Sessions sportives avec gestion des places
- **Épreuves** : Compétitions spécifiques dans chaque discipline
- **Offres** : Packages commerciaux et types de billets

Fonctionnalités
---------------

- **CRUD complet** pour toutes les entités
- **Recherche avancée** (ex: disciplines par nom)
- **Relations optimisées** entre modèles
- **Validation des données** avec contraintes d'unicité
- **Permissions par rôles** (public, admin, employé)

.. toctree::
   :maxdepth: 2
   :caption: Composants du module API

   models/index
   serializers/index
   views/index