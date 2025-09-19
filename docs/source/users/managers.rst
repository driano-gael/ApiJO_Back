Gestionnaires (Managers)
========================

Ce module contient les gestionnaires personnalisés pour la gestion des utilisateurs.

UserManager
-----------

.. autoclass:: users.managers.UserManager
   :members:
   :undoc-members:
   :show-inheritance:

   **Exemple d'utilisation :**

   .. code-block:: python

      from users.managers import UserManager

      # Créer un utilisateur standard
      user = UserManager().create_user(
          email="user@example.com",
          password="motdepasse123"
      )

      # Créer un administrateur
      admin = UserManager().create_admin(
          email="admin@example.com",
          password="motdepasse123"
      )

      # Créer un superutilisateur
      superuser = UserManager().create_superuser(
          email="super@example.com",
          password="motdepasse123"
      )

   **Notes importantes :**

   - Tous les utilisateurs sont identifiés par leur adresse email plutôt que par un nom d'utilisateur
   - L'email est normalisé automatiquement lors de la création
   - Les rôles sont définis via le champ ``role`` du modèle User
   - Les superutilisateurs ont automatiquement les permissions ``is_staff`` et ``is_superuser`` activées
