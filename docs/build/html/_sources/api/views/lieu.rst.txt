Vues Lieu
==========

LieuListView
~~~~~~~~~~~~

**Endpoint :** ``GET /api/lieu/``

- Liste tous les lieux disponibles
- **Permissions** : Accessible à tous

.. autoclass:: api.views.lieu.LieuListView
   :members:
   :undoc-members:
   :show-inheritance:

LieuDetailView
~~~~~~~~~~~~~~

**Endpoint :** ``GET /api/lieu/{id}/``

- Récupère un lieu par son ID
- **Permissions** : Accessible à tous

.. autoclass:: api.views.lieu.LieuDetailView
   :members:
   :undoc-members:
   :show-inheritance:

LieuCreateView
~~~~~~~~~~~~~~

**Endpoint :** ``POST /api/lieu/create/``

- Crée un nouveau lieu sportif
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.lieu.LieuCreateView
   :members:
   :undoc-members:
   :show-inheritance:

LieuUpdateView
~~~~~~~~~~~~~~

**Endpoint :** ``PUT/PATCH /api/lieu/update/{id}/``

- Met à jour un lieu existant
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.lieu.LieuUpdateView
   :members:
   :undoc-members:
   :show-inheritance:

LieuDeleteView
~~~~~~~~~~~~~~

**Endpoint :** ``DELETE /api/lieu/delete/{id}/``

- Supprime un lieu
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.lieu.LieuDeleteView
   :members:
   :undoc-members:
   :show-inheritance:

