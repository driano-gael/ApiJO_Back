Sérialiseurs API
================

Les sérialiseurs gèrent la conversion entre les objets Django et les représentations JSON pour l'API REST.

Fonctionnalités
---------------

- **Validation des données** avant création/mise à jour
- **Relations optimisées** entre entités (sérialiseurs imbriqués)
- **Champs séparés** lecture/écriture pour les clés étrangères
- **Gestion des conflits** (ex: épreuves déjà assignées)

.. toctree::
   :maxdepth: 2
   :caption: Sérialiseurs disponibles

   discipline
   lieu
   evenement
   epreuve
   offre
   nested_serializer
