Gestionnaires (Managers)
========================

Ce module contient les gestionnaires personnalisés pour la gestion des utilisateurs.


.. autoclass:: users.managers.UserManager
   :members:
   :undoc-members:
   :show-inheritance:



   **Notes importantes :**

   - Tous les utilisateurs sont identifiés par leur adresse email plutôt que par un nom d'utilisateur
   - L'email est normalisé automatiquement lors de la création
   - Les rôles sont définis via le champ ``role`` du modèle User
   - Les superutilisateurs ont automatiquement les permissions ``is_staff`` et ``is_superuser`` activées
