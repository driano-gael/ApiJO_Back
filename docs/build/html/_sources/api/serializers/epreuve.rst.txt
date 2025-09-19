Sérialiseur Epreuve
===================

.. autoclass:: api.serializers.epreuve.EpreuveSerializer
   :members:
   :undoc-members:
   :show-inheritance:


***Fonctionnalités***

- **Relations optimisées** : Affichage complet de la discipline et de l'événement
- **Validation d'unicité** : Évite les doublons d'épreuves par discipline
- **Champs séparés** lecture/écriture pour les clés étrangères
- **Assignation optionnelle** à un événement


***Validation spéciale***

La méthode ``validate()`` vérifie qu'aucune épreuve avec le même libellé n'existe déjà pour la même discipline.