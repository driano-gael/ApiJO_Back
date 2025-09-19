Vues API
========

Les vues gèrent les endpoints HTTP de l'API REST avec des opérations CRUD complètes.

Architecture des vues
---------------------

Toutes les vues suivent le même pattern :

- **ListView** : GET pour lister toutes les entités (accessible à tous)
- **DetailView** : GET pour récupérer une entité par ID (accessible à tous)
- **CreateView** : POST pour créer une nouvelle entité (admin uniquement)
- **UpdateView** : PUT/PATCH pour modifier une entité (admin uniquement)
- **DeleteView** : DELETE pour supprimer une entité (admin uniquement)

Permissions
-----------

- **Lecture** (GET) : Accessible à tous les utilisateurs
- **Écriture** (POST/PUT/DELETE) : Réservée aux administrateurs authentifiés

Fonctionnalités spéciales
-------------------------

- **Recherche** : Vue DisciplineListView avec paramètre ?search=
- **Tri optimisé** : Requêtes avec select_related() pour les performances
- **Vue custom** : EvenementByEpreuveView pour récupérer un événement par épreuve

.. toctree::
   :maxdepth: 2
   :caption: Vues disponibles

   discipline
   lieu
   evenement
   epreuve
   offre
