Sérialiseur Evenement
=====================

.. automodule:: api.serializers.evenement
   :members:
   :undoc-members:
   :show-inheritance:


***Fonctionnalités avancées***

- **Relations optimisées** : Affichage complet du lieu et des épreuves
- **Champs séparés** lecture/écriture pour les clés étrangères
- **Validation des conflits** : Évite l'assignation d'épreuves déjà utilisées
- **Gestion transactionnelle** : Mise à jour cohérente des relations


***Validations spéciales***

La méthode ``validate_epreuve_ids()`` vérifie qu'aucune épreuve n'est déjà assignée à un autre événement.