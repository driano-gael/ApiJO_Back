Vues Evenement
==============


EvenementListView
~~~~~~~~~~~~~~~~~

**Endpoint :** ``GET /api/evenement/``

- Liste tous les événements disponibles
- **Permissions** : Accessible à tous

.. autoclass:: api.views.evenement.EvenementListView
   :members:
   :undoc-members:
   :show-inheritance:

EvenementDetailView
~~~~~~~~~~~~~~~~~~~

**Endpoint :** ``GET /api/evenement/{id}/``

- Récupère un événement par son ID
- Inclut les épreuves associées et les informations du lieu
- **Permissions** : Accessible à tous

.. autoclass:: api.views.evenement.EvenementDetailView
   :members:
   :undoc-members:
   :show-inheritance:

EvenementByEpreuveView
~~~~~~~~~~~~~~~~~~~~~~

**Endpoint :** ``GET /api/evenement/by-epreuve/{epreuve_id}/``

- **Vue spécialisée** : Récupère l'événement associé à une épreuve
- Retourne 404 si aucun événement n'est associé à l'épreuve
- **Permissions** : Accessible à tous

.. autoclass:: api.views.evenement.EvenementByEpreuveView
   :members:
   :undoc-members:
   :show-inheritance:

EvenementCreateView
~~~~~~~~~~~~~~~~~~~

**Endpoint :** ``POST /api/evenement/create/``

- Crée un nouvel événement
- Permet d'assigner des épreuves lors de la création
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.evenement.EvenementCreateView
   :members:
   :undoc-members:
   :show-inheritance:

EvenementUpdateView
~~~~~~~~~~~~~~~~~~~

**Endpoint :** ``PUT/PATCH /api/evenement/update/{id}/``

- Met à jour un événement existant
- Gère la réassignation d'épreuves avec validation des conflits
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.evenement.EvenementUpdateView
   :members:
   :undoc-members:
   :show-inheritance:

EvenementDeleteView
~~~~~~~~~~~~~~~~~~~

**Endpoint :** ``DELETE /api/evenement/delete/{id}/``

- Supprime un événement
- **Permissions** : Admin authentifié uniquement

.. autoclass:: api.views.evenement.EvenementDeleteView
   :members:
   :undoc-members:
   :show-inheritance:

