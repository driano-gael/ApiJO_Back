Vues Discipline
===============


DisciplineListView
~~~~~~~~~~~~~~~~~~

**Endpoint :** ``GET /api/discipline/``

- Liste toutes les disciplines triées par nom
- **Recherche** : Paramètre ``?search=`` pour filtrer par nom (insensible à la casse)
- **Optimisation** : Utilise ``select_related()`` pour les performances
- **Permissions** : Accessible à tous


.. autoclass:: api.views.discipline.DisciplineListView
   :members:
   :undoc-members:
   :show-inheritance:


DisciplineDetailView
~~~~~~~~~~~~~~~~~~~~

**Endpoint :** ``GET /api/discipline/{id}/``

- Récupère une discipline par son ID
- **Permissions** : Accessible à tous


.. autoclass:: api.views.discipline.DisciplineDetailView
   :members:
   :undoc-members:
   :show-inheritance:

DisciplineCreateView
~~~~~~~~~~~~~~~~~~~~

**Endpoint :** ``POST /api/discipline/create/``

- Crée une nouvelle discipline
- **Permissions** : Admin authentifié uniquement


.. autoclass:: api.views.discipline.DisciplineCreateView
   :members:
   :undoc-members:
   :show-inheritance:

DisciplineUpdateView
~~~~~~~~~~~~~~~~~~~~

**Endpoint :** ``PUT/PATCH /api/discipline/update/{id}/``

- Met à jour une discipline existante
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.discipline.DisciplineUpdateView
   :members:
   :undoc-members:
   :show-inheritance:

DisciplineDeleteView
~~~~~~~~~~~~~~~~~~~~

**Endpoint :** ``DELETE /api/discipline/delete/{id}/``

- Supprime une discipline
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.discipline.DisciplineDeleteView
   :members:
   :undoc-members:
   :show-inheritance:

