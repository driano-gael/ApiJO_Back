Vues Epreuve
============

EpreuveListView
~~~~~~~~~~~~~~~

**Endpoint :** ``GET /api/epreuve/``

- Liste toutes les épreuves avec **tri optimisé** :
  - Par nom de discipline
  - Par date d'événement
  - Par horaire d'événement
- **Optimisation** : Utilise ``select_related("evenement", "discipline")``
- **Permissions** : Accessible à tous

.. autoclass:: api.views.epreuve.EpreuveListView
   :members:
   :undoc-members:
   :show-inheritance:

EpreuveDetailView
~~~~~~~~~~~~~~~~~

**Endpoint :** ``GET /api/epreuve/{id}/``

- Récupère une épreuve par son ID
- Inclut les informations de la discipline et de l'événement associé
- **Permissions** : Accessible à tous

.. autoclass:: api.views.epreuve.EpreuveDetailView
   :members:
   :undoc-members:
   :show-inheritance:

EpreuveCreateView
~~~~~~~~~~~~~~~~~

**Endpoint :** ``POST /api/epreuve/create/``

- Crée une nouvelle épreuve
- **Validation** : Évite les doublons par discipline
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.epreuve.EpreuveCreateView
   :members:
   :undoc-members:
   :show-inheritance:

EpreuveUpdateView
~~~~~~~~~~~~~~~~~

**Endpoint :** ``PUT/PATCH /api/epreuve/update/{id}/``

- Met à jour une épreuve existante
- **Validation** : Contrôle d'unicité maintenu
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.epreuve.EpreuveUpdateView
   :members:
   :undoc-members:
   :show-inheritance:

EpreuveDeleteView
~~~~~~~~~~~~~~~~~

**Endpoint :** ``DELETE /api/epreuve/delete/{id}/``

- Supprime une épreuve
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.epreuve.EpreuveDeleteView
   :members:
   :undoc-members:
   :show-inheritance:

