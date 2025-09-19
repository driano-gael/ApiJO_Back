Vues Offre
==========

Vues disponibles
----------------

OffreListView
~~~~~~~~~~~~~

**Endpoint :** ``GET /api/offre/``

- Liste toutes les offres avec **tri optimisé** :
  - Par nombre de personnes (croissant)
  - Par montant (croissant)
- **Permissions** : Accessible à tous

.. autoclass:: api.views.offre.OffreListView
   :members:
   :undoc-members:
   :show-inheritance:

OffreDetailView
~~~~~~~~~~~~~~~

**Endpoint :** ``GET /api/offre/{id}/``

- Récupère une offre par son ID
- **Permissions** : Accessible à tous

.. autoclass:: api.views.offre.OffreDetailView
   :members:
   :undoc-members:
   :show-inheritance:

OffreCreateView
~~~~~~~~~~~~~~~

**Endpoint :** ``POST /api/offre/create/``

- Crée une nouvelle offre commerciale
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.offre.OffreCreateView
   :members:
   :undoc-members:
   :show-inheritance:

OffreUpdateView
~~~~~~~~~~~~~~~

**Endpoint :** ``PUT/PATCH /api/offre/update/{id}/``

- Met à jour une offre existante
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.offre.OffreUpdateView
   :members:
   :undoc-members:
   :show-inheritance:

OffreDeleteView
~~~~~~~~~~~~~~~

**Endpoint :** ``DELETE /api/offre/delete/{id}/``

- Supprime une offre
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.offre.OffreDeleteView
   :members:
   :undoc-members:
   :show-inheritance:

